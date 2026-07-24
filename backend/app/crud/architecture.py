from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.analysis import Analysis
from app.models.architecture import Architecture


def create_architecture(
    db: Session,
    analysis: Analysis,
    architecture_data: dict,
    layers: str | None,
    dependencies: str | None,
) -> Architecture:

    db_architecture = Architecture(
        analysis_id=analysis.id,
        architecture_data=architecture_data,
        layers=layers,
        dependencies=dependencies,
    )

    db.add(db_architecture)
    db.commit()
    db.refresh(db_architecture)

    return db_architecture


def get_architecture(
    db: Session,
    analysis: Analysis,
) -> Architecture | None:

    stmt = (
        select(Architecture)
        .where(Architecture.analysis_id == analysis.id)
    )

    return db.execute(stmt).scalar_one_or_none()


def delete_architecture(
    db: Session,
    architecture: Architecture,
) -> None:

    db.delete(architecture)
    db.commit()