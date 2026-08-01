from __future__ import annotations

import uuid

from app.crud.project import (
    create_project,
    delete_project,
    get_project_by_id,
    get_projects_by_user,
)
from app.models.project import Project
from app.models.user import User
from app.schemas.project import ProjectCreate
from app.services.storage_service import delete_project_files
from sqlalchemy.orm import Session


def is_project_owner(
    user: User,
    project: Project,
) -> bool:

    return project.user_id == user.id


def create_user_project(
    db: Session,
    user: User,
    project_data: ProjectCreate,
    original_file_name: str,
    storage_path: str,
) -> Project:

    return create_project(
        db=db,
        user=user,
        name=project_data.name,
        description=project_data.description,
        original_file_name=original_file_name,
        storage_path=storage_path,
    )  


def get_user_projects(
    db: Session,
    user: User,
) -> list[Project]:

    return get_projects_by_user(
        db=db,
        user=user,
    )


def get_user_project(
    db: Session,
    user: User,
    project_id: uuid.UUID,
) -> Project | None:

    project = get_project_by_id(
        db=db,
        project_id=project_id,
    )

    if project is None:
        return None

    if not is_project_owner(
        user=user,
        project=project,
    ):
        return None

    return project


def delete_user_project(
    db: Session,
    user: User,
    project: Project,
) -> bool:

    if not is_project_owner(
        user=user,
        project=project,
    ):
        return False

    delete_project_files(
        storage_path=project.storage_path,
    )

    delete_project(
        db=db,
        project=project,
    )

    return True