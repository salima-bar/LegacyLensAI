from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ArchitectureRead(BaseModel):
    id: UUID
    analysis_id: UUID

    architecture_data: dict

    layers: str | None = None
    dependencies: str | None = None

    model_config = ConfigDict(from_attributes=True)