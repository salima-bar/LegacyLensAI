from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.analysis import Analysis
from app.models.roadmap import Roadmap


def create_roadmap(
    db: Session,
    analysis: Analysis,
    roadmap_data: dict,
) -> Roadmap:

    db_roadmap = Roadmap(
        analysis_id=analysis.id,
        roadmap_data=roadmap_data,
    )

    db.add(db_roadmap)
    db.commit()
    db.refresh(db_roadmap)

    return db_roadmap


def get_roadmap(
    db: Session,
    analysis: Analysis,
) -> Roadmap | None:

    stmt = (
        select(Roadmap)
        .where(Roadmap.analysis_id == analysis.id)
    )

    return db.execute(stmt).scalar_one_or_none()


def delete_roadmap(
    db: Session,
    roadmap: Roadmap,
) -> None:

    db.delete(roadmap)
    db.commit()