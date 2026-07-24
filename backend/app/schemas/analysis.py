from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AnalysisBase(BaseModel):
    summary: str | None = None
    detected_technologies: str | None = None
    programming_language: str | None = None
    framework: str | None = None


class AnalysisCreate(BaseModel):
    pass


class AnalysisRead(AnalysisBase):
    id: UUID
    project_id: UUID
    version: int
    analysis_date: datetime

    model_config = ConfigDict(from_attributes=True)
    