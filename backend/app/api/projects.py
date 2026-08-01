from __future__ import annotations

from typing import Annotated
from uuid import UUID

from app.api.dependencies import get_current_user, get_db
from app.models.user import User
from app.schemas.project import (
    ProjectCreate,
    ProjectRead,
)
from app.services.project_service import (
    create_user_project,
    delete_user_project,
    get_user_project,
    get_user_projects,
)
from app.services.storage_service import save_uploaded_project
from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    HTTPException,
    Response,
    UploadFile,
    status,
)
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)

Database = Annotated[
    Session,
    Depends(get_db),
]

CurrentUser = Annotated[
    User,
    Depends(get_current_user),
]

ProjectArchive = Annotated[
    UploadFile,
    File(...),
]

ProjectName = Annotated[
    str,
    Form(...),
]

ProjectDescription = Annotated[
    str | None,
    Form(),
]

@router.post(
    "",
    response_model=ProjectRead,
    status_code=status.HTTP_201_CREATED,
)
def create_project(
    name: ProjectName,
    description: ProjectDescription = None,
    project_archive: ProjectArchive = None,
    db: Database = None,
    current_user: CurrentUser = None,
) -> ProjectRead:
    """
    Upload a new project.
    """

    if not project_archive.filename.lower().endswith(".zip"):

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only ZIP archives are supported.",
        )

    project_data = ProjectCreate(
        name=name,
        description=description,
    )

    storage_path = save_uploaded_project(
        uploaded_file=project_archive,
    )

    return create_user_project(
        db=db,
        user=current_user,
        project_data=project_data,
        original_file_name=project_archive.filename,
        storage_path=storage_path,
    )

@router.get(
    "",
    response_model=list[ProjectRead],
)
def get_projects(
    db: Database = None,
    current_user: CurrentUser = None,
) -> list[ProjectRead]:
    """
    Return all projects belonging to the authenticated user.
    """

    return get_user_projects(
        db=db,
        user=current_user,
    )

@router.get(
    "/{project_id}",
    response_model=ProjectRead,
)
def get_project(
    project_id: UUID,
    db: Database = None,
    current_user: CurrentUser = None,
) -> ProjectRead:
    """
    Return one project owned by the authenticated user.
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

    return project

@router.delete(
    "/{project_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_project(
    project_id: UUID,
    db: Database = None,
    current_user: CurrentUser = None,
) -> Response:
    """
    Delete one project owned by the authenticated user.
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

    delete_user_project(
        db=db,
        user=current_user,
        project=project,
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )