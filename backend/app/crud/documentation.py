from __future__ import annotations

from app.models.analysis import Analysis
from app.models.documentation import Documentation
from sqlalchemy import select
from sqlalchemy.orm import Session


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