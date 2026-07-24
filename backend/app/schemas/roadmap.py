from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class RoadmapRead(BaseModel):
    id: UUID
    analysis_id: UUID

    roadmap_data: dict

    generated_at: datetime

    model_config = ConfigDict(from_attributes=True)