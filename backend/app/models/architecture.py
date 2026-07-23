from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Text, text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.models.analysis import Analysis 

class Architecture(Base):
    __tablename__ = "architectures"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )

    analysis_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("analyses.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    architecture_data: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False,
    )

    layers: Mapped[str | None] = mapped_column(
        Text,
    )

    dependencies: Mapped[str | None] = mapped_column(
        Text,
    )

    # Relationship

    analysis: Mapped["Analysis"] = relationship(
        back_populates="architecture",
    )