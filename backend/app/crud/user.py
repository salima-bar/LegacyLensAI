from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


def create_user(
    db: Session,
    user: UserCreate,
    password_hash: str,
) -> User:

    db_user = User(
        full_name=user.full_name,
        email=user.email,
        password_hash=password_hash,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user_by_id(
    db: Session,
    user_id: UUID,
) -> User | None:

    stmt = select(User).where(User.id == user_id)

    return db.execute(stmt).scalar_one_or_none()


def get_user_by_email(
    db: Session,
    email: str,
) -> User | None:

    stmt = select(User).where(User.email == email)

    return db.execute(stmt).scalar_one_or_none()


def update_user(
    db: Session,
    db_user: User,
    user_update: UserUpdate,
) -> User:

    update_data = user_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user(
    db: Session,
    db_user: User,
) -> None:

    db.delete(db_user)
    db.commit()