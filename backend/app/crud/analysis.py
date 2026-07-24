from __future__ import annotations

from uuid import UUID

from sqlalchemy import desc, select
from sqlalchemy.orm import Session

from app.models.analysis import Analysis
from app.models.project import Project


def create_analysis(
    db: Session,
    project: Project,
    version: int,
    summary: str | None,
    detected_technologies: str | None,
    programming_language: str | None,
    framework: str | None,
) -> Analysis:

    db_analysis = Analysis(
        project_id=project.id,
        version=version,
        summary=summary,
        detected_technologies=detected_technologies,
        programming_language=programming_language,
        framework=framework,
    )

    db.add(db_analysis)
    db.commit()
    db.refresh(db_analysis)

    return db_analysis


def get_analysis_by_id(
    db: Session,
    analysis_id: UUID,
) -> Analysis | None:

    stmt = select(Analysis).where(Analysis.id == analysis_id)

    return db.execute(stmt).scalar_one_or_none()


def get_project_analyses(
    db: Session,
    project: Project,
) -> list[Analysis]:

    stmt = (
        select(Analysis)
        .where(Analysis.project_id == project.id)
        .order_by(desc(Analysis.version))
    )

    return list(db.execute(stmt).scalars().all())


def get_latest_analysis(
    db: Session,
    project: Project,
) -> Analysis | None:

    stmt = (
        select(Analysis)
        .where(Analysis.project_id == project.id)
        .order_by(desc(Analysis.version))
        .limit(1)
    )

    return db.execute(stmt).scalar_one_or_none()


def delete_analysis(
    db: Session,
    analysis: Analysis,
) -> None:

    db.delete(analysis)
    db.commit()