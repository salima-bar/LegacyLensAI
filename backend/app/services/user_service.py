from __future__ import annotations

from app.crud.user import (
    create_user,
    delete_user,
    get_user_by_email,
    update_user,
)
from app.models.user import User
from app.schemas.user import (
    UserCreate,
    UserUpdate,
)
from app.services.auth_service import hash_password
from sqlalchemy.orm import Session


def register_user(
    db: Session,
    user_data: UserCreate,
) -> User | None:

    existing_user = get_user_by_email(
        db=db,
        email=user_data.email,
    )

    if existing_user is not None:
        return None

    password_hash = hash_password(
        user_data.password,
    )

    return create_user(
        db=db,
        user=user_data,
        password_hash=password_hash,
    )


def get_user_profile(
    user: User,
) -> User:

    return user


def update_user_profile(
    db: Session,
    user: User,
    user_data: UserUpdate,
) -> User:

    return update_user(
        db=db,
        db_user=user,
        user_update=user_data,
    )


def delete_user_account(
    db: Session,
    user: User,
) -> None:

    delete_user(
        db=db,
        db_user=user,
    )