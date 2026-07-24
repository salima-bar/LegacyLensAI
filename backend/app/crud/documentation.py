from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.analysis import Analysis
from app.models.documentation import Documentation


def create_documentation(
    db: Session,
    analysis: Analysis,
    content: str,
) -> Documentation:

    db_documentation = Documentation(
        analysis_id=analysis.id,
        content=content,
    )

    db.add(db_documentation)
    db.commit()
    db.refresh(db_documentation)

    return db_documentation


def get_documentation(
    db: Session,
    analysis: Analysis,
) -> Documentation | None:

    stmt = (
        select(Documentation)
        .where(Documentation.analysis_id == analysis.id)
    )

    return db.execute(stmt).scalar_one_or_none()


def delete_documentation(
    db: Session,
    documentation: Documentation,
) -> None:

    db.delete(documentation)
    db.commit()