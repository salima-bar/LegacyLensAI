from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
    Text,
    DateTime,
    Enum,
    ForeignKey,
    text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import Base
from app.models.enums import ProjectStatus

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.analysis import Analysis

class Project(Base):
    __tablename__ = "projects"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
    Text,
    nullable=True,
)

    original_file_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    storage_path: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    status: Mapped[ProjectStatus] = mapped_column(
        Enum(ProjectStatus, name="project_status"),
        nullable=False,
        server_default=text("'Uploaded'"),
    )

    upload_date: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )

    last_analysis_date: Mapped[datetime | None] = mapped_column(
        DateTime,
    )

    current_analysis_id: Mapped[uuid.UUID | None] = mapped_column( 
        UUID(as_uuid=True), 
        ForeignKey("analyses.id", ondelete="SET NULL"), 
    )

    # Relationships

    user: Mapped["User"] = relationship(
        back_populates="projects",
    )

    analyses: Mapped[list["Analysis"]] = relationship(
        back_populates="project",
        cascade="all, delete-orphan",
        foreign_keys="Analysis.project_id",
    )

    # Latest analysis for this project
    current_analysis: Mapped["Analysis | None"] = relationship(
        foreign_keys=[current_analysis_id],
        uselist=False,
    )