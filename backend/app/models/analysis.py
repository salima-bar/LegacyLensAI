from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
    UniqueConstraint,
    text,
)

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import Base

if TYPE_CHECKING:
    from app.models.project import Project
    from app.models.documentation import Documentation
    from app.models.architecture import Architecture
    from app.models.roadmap import Roadmap
    from app.models.recommendation import Recommendation
    

class Analysis(Base):
    __tablename__ = "analyses"

    __table_args__ = (
        UniqueConstraint(
            "project_id",
            "version",
            name="uq_project_version",
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )

    project_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
    )

    version: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    summary: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    detected_technologies: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    programming_language: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    framework: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    analysis_date: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )

    # Relationships
    
    # Parent project
    project: Mapped["Project"] = relationship(
        back_populates="analyses",
        foreign_keys=[project_id],
    )

    # One-to-one
    architecture: Mapped["Architecture | None"] = relationship(
        back_populates="analysis",
        cascade="all, delete-orphan",
        uselist=False,
    )

    # One-to-one
    documentation: Mapped["Documentation | None"] = relationship(
        back_populates="analysis",
        cascade="all, delete-orphan",
        uselist=False,
    )
    
    # One-to-one
    roadmap: Mapped["Roadmap | None"] = relationship(
        back_populates="analysis",
        cascade="all, delete-orphan",
        uselist=False,
    )

    # One-to-many (list)
    recommendations: Mapped[list["Recommendation"]] = relationship(
        back_populates="analysis",
        cascade="all, delete-orphan",
    )