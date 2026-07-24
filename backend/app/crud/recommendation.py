from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.analysis import Analysis
from app.models.enums import (
    RecommendationCategory,
    RecommendationComponent,
    RecommendationPriority,
)
from app.models.recommendation import Recommendation


def create_recommendation(
    db: Session,
    analysis: Analysis,
    title: str,
    description: str,
    component: RecommendationComponent,
    priority: RecommendationPriority,
    category: RecommendationCategory | None,
) -> Recommendation:

    db_recommendation = Recommendation(
        analysis_id=analysis.id,
        title=title,
        description=description,
        component=component,
        priority=priority,
        category=category,
    )

    db.add(db_recommendation)
    db.commit()
    db.refresh(db_recommendation)

    return db_recommendation


def get_recommendations(
    db: Session,
    analysis: Analysis,
) -> list[Recommendation]:

    stmt = (
        select(Recommendation)
        .where(Recommendation.analysis_id == analysis.id)
    )

    return list(db.execute(stmt).scalars().all())


def delete_recommendations(
    db: Session,
    recommendations: list[Recommendation],
) -> None:

    for recommendation in recommendations:
        db.delete(recommendation)

    db.commit()