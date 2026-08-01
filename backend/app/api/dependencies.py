from __future__ import annotations

from typing import Annotated
from uuid import UUID

from app.ai.assistant import ProjectAssistant
from app.ai.llm import LLMClient
from app.core.config import settings
from app.crud.user import get_user_by_id
from app.database.dependencies import get_db
from app.models.user import User
from app.schemas.auth import TokenData
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login",
)

def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[Session, Depends(get_db)],
) -> User:
    """
    Return the authenticated user from the JWT access token.
    """

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )

        user_id = payload.get("sub")

        if user_id is None:
            raise credentials_exception

        token_data = TokenData(
            user_id=user_id,
        )

    except JWTError:
        raise credentials_exception

    user = get_user_by_id(
        db=db,
        user_id=UUID(token_data.user_id),
    )

    if user is None:
        raise credentials_exception

    return user

def get_llm() -> LLMClient:
    """
    Return the language model client.
    """
    return LLMClient()

def get_project_assistant() -> ProjectAssistant:
    """
    Return the AI project assistant.
    """

    return ProjectAssistant(
        llm=get_llm(),
    )