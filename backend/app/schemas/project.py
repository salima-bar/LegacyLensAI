from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.models.enums import ProjectStatus


# ===========================
# Base Schema
# ===========================

class ProjectBase(BaseModel):
    name: str
    description: str | None = None


# ===========================
# Create
# ===========================

class ProjectCreate(ProjectBase):
    pass


# ===========================
# Update
# ===========================

class ProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None


# ===========================
# Read
# ===========================

class ProjectRead(ProjectBase):
    id: UUID
    user_id: UUID

    original_file_name: str

    status: ProjectStatus

    upload_date: datetime
    last_analysis_date: datetime | None

    current_analysis_id: UUID | None

    model_config = ConfigDict(from_attributes=True)