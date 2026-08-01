from __future__ import annotations

from typing import Annotated
from uuid import UUID

from app.api.dependencies import get_current_user
from app.crud.architecture import get_architecture
from app.database.dependencies import get_db
from app.models.user import User
from app.schemas.analysis import AnalysisRead
from app.schemas.architecture import DiagramPayload
from app.services.analysis_service import (
    AnalysisAlreadyRunningError,
    get_analysis,
    get_analysis_history,
    get_project_analysis,
    start_analysis,
)
from app.services.project_service import get_user_project
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"],
)

Database = Annotated[
    Session,
    Depends(get_db),
]

CurrentUser = Annotated[
    User,
    Depends(get_current_user),
]

@router.post(
    "/{project_id}",
    response_model=AnalysisRead,
    status_code=status.HTTP_201_CREATED,
)
def analyze_project(
    project_id: UUID,
    db: Database = None,
    current_user: CurrentUser = None,
) -> AnalysisRead:
    """
    Start AI analysis for one project.
    """

    project = get_user_project(
        db=db,
        user=current_user,
        project_id=project_id,
    )

    if project is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found.",
        )

    try:

        return start_analysis(
            db=db,
            project=project,
        )

    except AnalysisAlreadyRunningError as exc:

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc

@router.get(
    "/{project_id}",
    response_model=AnalysisRead,
)
def get_project_latest_analysis(
    project_id: UUID,
    db: Database = None,
    current_user: CurrentUser = None,
) -> AnalysisRead:
    """
    Return the latest analysis for a project.
    """

    project = get_user_project(
        db=db,
        user=current_user,
        project_id=project_id,
    )

    if project is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found.",
        )

    analysis = get_project_analysis(
        db=db,
        project=project,
    )

    if analysis is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No analysis found for this project.",
        )

    return analysis

@router.get(
    "/result/{analysis_id}",
    response_model=AnalysisRead,
)
def get_analysis_result(
    analysis_id: UUID,
    db: Database = None,
    current_user: CurrentUser = None,
) -> AnalysisRead:
    """
    Return one analysis by its identifier.
    """

    analysis = get_analysis(
        db=db,
        user=current_user,
        analysis_id=analysis_id,
    )

    if analysis is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Analysis not found.",
        )

    return analysis

@router.get(
    "/history/{project_id}",
    response_model=list[AnalysisRead],
)
def get_project_analysis_history(
    project_id: UUID,
    db: Database = None,
    current_user: CurrentUser = None,
) -> list[AnalysisRead]:
    """
    Return all analyses of a project.
    """

    project = get_user_project(
        db=db,
        user=current_user,
        project_id=project_id,
    )

    if project is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found.",
        )

    return get_analysis_history(
        db=db,
        project=project,
    )


@router.get(
    "/diagram/{analysis_id}",
    response_model=DiagramPayload,
)
def get_analysis_diagram(
    analysis_id: UUID,
    db: Database = None,
    current_user: CurrentUser = None,
) -> DiagramPayload:
    """
    Return a frontend-friendly diagram payload for the analysis.
    """

    analysis = get_analysis(
        db=db,
        user=current_user,
        analysis_id=analysis_id,
    )

    if analysis is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Analysis not found.",
        )

    architecture = get_architecture(
        db=db,
        analysis=analysis,
    )

    if architecture is None:
        return DiagramPayload(nodes=[], edges=[])

    return build_diagram_payload(architecture.architecture_data)


def build_diagram_payload(diagram_data: dict | None) -> dict[str, list[dict[str, object]]]:
    """
    Normalize AI-generated architecture data into a React Flow-friendly payload.
    """

    if not isinstance(diagram_data, dict):
        return {"nodes": [], "edges": []}

    raw_nodes = diagram_data.get("nodes", [])
    raw_edges = diagram_data.get("edges", [])

    if not isinstance(raw_nodes, list):
        raw_nodes = []

    if not isinstance(raw_edges, list):
        raw_edges = []

    nodes: list[dict] = []
    for index, node in enumerate(raw_nodes):
        if not isinstance(node, dict):
            continue

        node_id = str(node.get("id") or f"node-{index}")
        position = node.get("position") or {}
        x = 0.0
        y = 0.0

        if isinstance(position, dict):
            x = float(position.get("x", 0) or 0)
            y = float(position.get("y", 0) or 0)

        normalized_node: dict[str, object] = {
            "id": node_id,
            "position": {"x": x, "y": y},
            "data": dict(node.get("data") or {}),
        }

        if node.get("type"):
            normalized_node["type"] = str(node["type"])

        if node.get("style"):
            normalized_node["style"] = node["style"]

        nodes.append(normalized_node)

    edges: list[dict] = []
    for index, edge in enumerate(raw_edges):
        if not isinstance(edge, dict):
            continue

        source = edge.get("source")
        target = edge.get("target")

        if not source or not target:
            continue

        normalized_edge: dict[str, object] = {
            "id": str(edge.get("id") or f"edge-{index}"),
            "source": str(source),
            "target": str(target),
        }

        if edge.get("label"):
            normalized_edge["label"] = str(edge["label"])

        if edge.get("animated") is not None:
            normalized_edge["animated"] = bool(edge["animated"])

        if edge.get("style"):
            normalized_edge["style"] = edge["style"]

        edges.append(normalized_edge)

    return {"nodes": nodes, "edges": edges}