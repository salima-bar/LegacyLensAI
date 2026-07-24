from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class DocumentationRead(BaseModel):
    id: UUID
    analysis_id: UUID

    content: str

    generated_at: datetime

    model_config = ConfigDict(from_attributes=True)