from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Enum, ForeignKey, String, Text, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.models.enums import (
    RecommendationCategory,
    RecommendationPriority,
    RecommendationComponent,
)

if TYPE_CHECKING:
    from app.models.analysis import Analysis

class Recommendation(Base):
    __tablename__ = "recommendations"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )

    analysis_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("analyses.id", ondelete="CASCADE"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    component: Mapped[RecommendationPriority | None] = mapped_column(
        Enum(
            RecommendationComponent,
            name="recommendation_component",
        ),
    ) 

    priority: Mapped[RecommendationPriority | None] = mapped_column(
        Enum(
            RecommendationPriority,
            name="recommendation_priority",
        ),
    )

    category: Mapped[RecommendationCategory | None] = mapped_column(
        Enum(
            RecommendationCategory,
            name="recommendation_category",
        ),
    )

    # Relationship

    analysis: Mapped["Analysis"] = relationship(
        back_populates="recommendations",
    )