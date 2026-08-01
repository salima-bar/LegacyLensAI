from __future__ import annotations

from uuid import UUID

from app.ai.analysis import AnalysisEngine
from app.ai.context_builder import ContextBuilder
from app.ai.llm import LLMClient
from app.ai.parser import AnalysisParser
from app.ai.prompt_builder import PromptBuilder
from app.ai.result import (
    AnalysisResult,
    ArchitectureResult,
    ProjectFiles,
    RecommendationResult,
    RoadmapResult,
)

# ------------------------------------------------------------------
# CRUD
from app.crud.analysis import (
    create_analysis,
    get_analysis_by_id_and_user,
    get_latest_analysis,
    get_project_analyses,
)
from app.crud.architecture import create_architecture
from app.crud.documentation import create_documentation
from app.crud.project import (
    set_latest_analysis,
    update_project_status,
)
from app.crud.recommendation import create_recommendation
from app.crud.roadmap import create_roadmap

# Models and services
from app.models.analysis import Analysis
from app.models.enums import ProjectStatus
from app.models.project import Project
from app.models.user import User
from app.services.storage_service import read_project_files

# SQLAlchemy
from sqlalchemy.orm import Session

"""
Analysis Workflow

1. Update project status to Analyzing.
2. Read uploaded project files.
3. Send project to the AI engine.
4. Create analysis record.
5. Save architecture.
6. Save documentation.
7. Save roadmap.
8. Save recommendations.
9. Update latest analysis.
10. Update project status to Completed.
"""

class AnalysisAlreadyRunningError(Exception):
    """
    Raised when an analysis is already running for the project.
    """


def start_analysis(
    db: Session,
    project: Project,
) -> Analysis:
    """
    Main orchestrator responsible for the complete
    project analysis workflow.
    """

    if project.status == ProjectStatus.ANALYZING:
        raise AnalysisAlreadyRunningError(
            "Project analysis is already in progress."
        )
    
    try:

        # ----------------------------------------------------------
        # Preparation
        # ----------------------------------------------------------

        _start_project_analysis(
            db=db,
            project=project,
        )

        # ----------------------------------------------------------
        # Read Project Files
        # ----------------------------------------------------------

        project_files = _read_project_files(
            project=project,
        )

        # ----------------------------------------------------------
        # AI Analysis
        # ----------------------------------------------------------

        ai_result = _generate_analysis(
            project_files=project_files,
        )

        # ----------------------------------------------------------
        # Save Analysis
        # ----------------------------------------------------------

        analysis = _create_analysis_record(
            db=db,
            project=project,
            ai_result=ai_result,
        )

        _save_architecture(
            db=db,
            analysis=analysis,
            ai_result=ai_result,
        )

        _save_documentation(
            db=db,
            analysis=analysis,
            ai_result=ai_result,
        )

        _save_roadmap(
            db=db,
            analysis=analysis,
            ai_result=ai_result,
        )

        _save_recommendations(
            db=db,
            analysis=analysis,
            ai_result=ai_result,
        )

        # ----------------------------------------------------------
        # Finalization
        # ----------------------------------------------------------

        _complete_project_analysis(
            db=db,
            project=project,
            analysis=analysis,
        )

        return analysis

    except Exception :

        _fail_project_analysis(
            db=db,
            project=project,
        )

        raise

def get_project_analysis(
    db: Session,
    project: Project,
) -> Analysis | None:
    """
    Return the latest analysis for a project.
    """

    return get_latest_analysis(
        db=db,
        project=project,
    )


def get_analysis(
    db: Session,
    user: User,
    analysis_id: UUID,
) -> Analysis | None:
    """
    Return one analysis by its identifier.
    """

    return get_analysis_by_id_and_user(
        db=db,
        analysis_id=analysis_id,
        user=user,
    )

def get_analysis_history(
    db: Session,
    project: Project,
) -> list[Analysis]:
    """
    Return all analyses for a project ordered
    from newest to oldest.
    """

    return get_project_analyses(
        db=db,
        project=project,
    ) 

# ==================================================================
# PRIVATE HELPERS
# ==================================================================


def _start_project_analysis(
    db: Session,
    project: Project,
) -> None:
    """
    Mark project as currently being analyzed.
    """

    update_project_status(
        db=db,
        project=project,
        status="Analyzing",
    )


def _read_project_files(
    project: Project,
) -> ProjectFiles:
    """
    Read uploaded project files.
    """

    return read_project_files(
        storage_path=project.storage_path,
        project_name=project.name,
    )


def _generate_analysis(
    project_files: ProjectFiles,
) -> AnalysisResult:
    """
    Send the project files to the AI analysis engine.
    """

    engine = AnalysisEngine(
        context_builder=ContextBuilder(),
        prompt_builder=PromptBuilder(),
        llm=LLMClient(),
        parser=AnalysisParser(),
    )

    return engine.analyze_project(project_files)


def _create_analysis_record(
    db: Session,
    project: Project,
    ai_result: AnalysisResult,
) -> Analysis:
    """
    Create Analysis database record.
    """
    latest_analysis = get_latest_analysis(
        db=db,
        project=project,
    )

    version = 1

    if latest_analysis is not None:
        version = latest_analysis.version + 1

    return create_analysis(
        db=db,
        project=project,
        version=version,
        summary=ai_result.summary,
        detected_technologies=ai_result.detected_technologies,
        programming_language=ai_result.programming_language,
        framework=ai_result.framework,
    )


def _save_architecture(
    db: Session,
    analysis: Analysis,
    ai_result: AnalysisResult,
) -> None:
    """
    Save generated architecture.
    """

    architecture: ArchitectureResult = ai_result.architecture

    create_architecture(
        db=db,
        analysis=analysis,
        architecture_data=architecture.diagram_data,
        layers=", ".join(architecture.layers) if architecture.layers else None,
        dependencies=", ".join(
            f"{dependency.source}->{dependency.target}"
            for dependency in architecture.dependencies
        ) if architecture.dependencies else None,
    )


def _save_documentation(
    db: Session,
    analysis: Analysis,
    ai_result: AnalysisResult,
) -> None:
    """
    Save generated documentation.
    """

    create_documentation(
        db=db,
        analysis=analysis,
        content=ai_result.documentation,
    )


def _save_roadmap(
    db: Session,
    analysis: Analysis,
    ai_result: AnalysisResult,
) -> None:
    """
    Save generated roadmap.
    """

    roadmap: RoadmapResult = ai_result.roadmap

    create_roadmap(
        db=db,
        analysis=analysis,
        roadmap_data=roadmap.roadmap_data,
    )


def _save_recommendations(
    db: Session,
    analysis: Analysis,
    ai_result: AnalysisResult,
) -> None:
    """
    Save generated recommendations.
    """

    recommendation: RecommendationResult = ai_result.recommendation

    create_recommendation(
        db=db,
        analysis=analysis,
        title=recommendation.title,
        description=recommendation.description,
        component=recommendation.component,
        priority=recommendation.priority,
        category=recommendation.category,
    )


def _complete_project_analysis(
    db: Session,
    project: Project,
    analysis: Analysis,
) -> None:
    """
    Finalize successful analysis.
    """

    set_latest_analysis(
        db=db,
        project=project,
        analysis=analysis,
    )

    update_project_status(
        db=db,
        project=project,
        status="Completed",
    )


def _fail_project_analysis(
    db: Session,
    project: Project,
) -> None:
    """
    Mark project analysis as failed.
    """

    update_project_status(
        db=db,
        project=project,
        status="Failed",
    )