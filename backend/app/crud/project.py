from __future__ import annotations

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.analysis import Analysis
from app.models.enums import ProjectStatus
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate


def create_project(
    db: Session,
    user_id: UUID,
    project: ProjectCreate,
    original_file_name: str,
    storage_path: str,
) -> Project:

    db_project = Project(
        user_id=user_id,
        name=project.name,
        description=project.description,
        original_file_name=original_file_name,
        storage_path=storage_path,
    )

    db.add(db_project)
    db.commit()
    db.refresh(db_project)

    return db_project


def get_project_by_id(
    db: Session,
    project_id: UUID,
) -> Project | None:

    stmt = select(Project).where(Project.id == project_id)

    return db.execute(stmt).scalar_one_or_none()


def get_projects_by_user(
    db: Session,
    user_id: UUID,
) -> list[Project]:

    stmt = (
        select(Project)
        .where(Project.user_id == user_id)
        .order_by(Project.upload_date.desc())
    )

    return list(db.execute(stmt).scalars().all())


def update_project(
    db: Session,
    db_project: Project,
    project_update: ProjectUpdate,
) -> Project:

    update_data = project_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_project, field, value)

    db.commit()
    db.refresh(db_project)

    return db_project


def update_project_status(
    db: Session,
    db_project: Project,
    status: ProjectStatus,
) -> Project:

    db_project.status = status

    db.commit()
    db.refresh(db_project)

    return db_project


def set_latest_analysis(
    db: Session,
    db_project: Project,
    analysis: Analysis,
) -> Project:

    db_project.current_analysis_id = analysis.id
    db_project.last_analysis_date = analysis.analysis_date

    db.commit()
    db.refresh(db_project)

    return db_project


def delete_project(
    db: Session,
    db_project: Project,
) -> None:

    db.delete(db_project)
    db.commit()