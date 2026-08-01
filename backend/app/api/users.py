from __future__ import annotations

from typing import Annotated

from app.api.dependencies import get_current_user
from app.database.dependencies import get_db
from app.models.user import User
from app.schemas.user import (
    UserCreate,
    UserRead,
    UserUpdate,
)
from app.services.user_service import (
    delete_user_account,
    get_user_profile,
    register_user,
    update_user_profile,
)
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

@router.post(
    "/register",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user_data: UserCreate,
    db: Annotated[Session, Depends(get_db)],
) -> UserRead:

    user = register_user(
        db=db,
        user_data=user_data,
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists.",
        )

    return user


@router.get(
    "/me",
    response_model=UserRead,
)
def read_profile(
    current_user: Annotated[
        User,
        Depends(get_current_user),
    ],
) -> UserRead:

    return get_user_profile(
        current_user,
    )

@router.put(
    "/me",
    response_model=UserRead,
)
def update_profile(
    user_data: UserUpdate,
    db: Annotated[Session, Depends(get_db)],
    current_user: Annotated[
        User,
        Depends(get_current_user),
    ],
) -> UserRead:

    return update_user_profile(
        db=db,
        user=current_user,
        user_data=user_data,
    )


@router.delete(
    "/me",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_profile(
    db: Annotated[Session, Depends(get_db)],
    current_user: Annotated[
        User,
        Depends(get_current_user),
    ],
) -> None:

    delete_user_account(
        db=db,
        user=current_user,
    )