from __future__ import annotations

from typing import Annotated
from uuid import UUID

from app.ai.assistant import ProjectAssistant
from app.ai.result import (
    AnalysisResult,
    ArchitectureResult,
    AssistantRequest,
    AssistantResponse,
    ConversationHistory,
    RecommendationResult,
    RoadmapResult,
)
from app.api.dependencies import get_current_user, get_project_assistant
from app.database.dependencies import get_db
from app.models.enums import (
    RecommendationCategory,
    RecommendationComponent,
    RecommendationPriority,
)
from app.models.user import User
from app.services.analysis_service import get_project_analysis
from app.services.project_service import get_user_project
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/assistant",
    tags=["Assistant"],
)

Database = Annotated[
    Session,
    Depends(get_db),
]

CurrentUser = Annotated[
    User,
    Depends(get_current_user),
]

AssistantService = Annotated[
    ProjectAssistant,
    Depends(get_project_assistant),
]


@router.post(
    "/{project_id}",
    response_model=AssistantResponse,
)
def chat_with_assistant(
    project_id: UUID,
    request: AssistantRequest,
    db: Database = None,
    current_user: CurrentUser = None,
    assistant: AssistantService = None,
) -> AssistantResponse:
    """
    Send a message to the AI assistant for the selected project.
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

    analysis_record = get_project_analysis(
        db=db,
        project=project,
    )

    if analysis_record is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No analysis found for this project.",
        )

    analysis = _build_analysis_result(analysis_record)
    history = request.history or ConversationHistory()

    return assistant.chat(
        analysis=analysis,
        history=history,
        message=request.message,
    )


def _build_analysis_result(analysis_record: object) -> AnalysisResult:
    """
    Create a lightweight analysis payload suitable for the assistant.
    """

    return AnalysisResult(
        summary=analysis_record.summary or "No summary available.",
        detected_technologies=(
            [item.strip() for item in (analysis_record.detected_technologies or "").split(",") if item.strip()]
        ),
        programming_languages=[],
        frameworks=[],
        architecture=ArchitectureResult(),
        documentation=analysis_record.summary or "No documentation available.",
        roadmap=RoadmapResult(),
        recommendation=RecommendationResult(
            title="Project recommendation",
            description="No recommendation data is available yet.",
            component=RecommendationComponent.ARCHITECTURE,
            priority=RecommendationPriority.MEDIUM,
            category=RecommendationCategory.BEST_PRACTICE,
        ),
    )

