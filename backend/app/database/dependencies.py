from __future__ import annotations

from collections.abc import Generator

from app.database.session import SessionLocal
from sqlalchemy.orm import Session


def get_db() -> Generator[Session, None, None]:
    """
    Create a database session for a single request.

    The session is automatically closed after the request
    is completed.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()