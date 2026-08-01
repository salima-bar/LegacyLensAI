from __future__ import annotations

from datetime import datetime, timedelta, timezone

from app.core.config import settings
from app.crud.user import get_user_by_email
from app.models.user import User
from jose import jwt
from pwdlib import PasswordHash
from sqlalchemy.orm import Session

password_hash = PasswordHash.recommended()


def hash_password(
    password: str,
) -> str:

    return password_hash.hash(password)


def verify_password(
    password: str,
    password_hash_value: str,
) -> bool:

    return password_hash.verify(password, password_hash_value)


def authenticate_user(
    db: Session,
    email: str,
    password: str,
) -> User | None:

    user = get_user_by_email(
        db=db,
        email=email,
    )

    if user is None:
        return None

    if not verify_password(
        password,
        user.password_hash,
    ):
        return None

    return user


def create_access_token(
    user: User,
) -> str:

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
    )

    payload = {
        "sub": str(user.id),
        "exp": expire,
    }

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )