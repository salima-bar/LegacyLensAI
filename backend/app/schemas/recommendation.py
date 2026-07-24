from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.models.enums import (
    RecommendationCategory,
    RecommendationComponent,
    RecommendationPriority,
)


class RecommendationRead(BaseModel):
    id: UUID

    analysis_id: UUID

    title: str
    description: str

    component: RecommendationComponent

    priority: RecommendationPriority

    category: RecommendationCategory | None = None

    model_config = ConfigDict(from_attributes=True)