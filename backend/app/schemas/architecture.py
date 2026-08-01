from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ArchitectureRead(BaseModel):
    id: UUID
    analysis_id: UUID

    architecture_data: dict

    layers: str | None = None
    dependencies: str | None = None

    model_config = ConfigDict(from_attributes=True)


class DiagramNode(BaseModel):
    id: str
    type: str | None = None
    position: dict[str, float] = Field(default_factory=lambda: {"x": 0.0, "y": 0.0})
    data: dict[str, Any] = Field(default_factory=dict)
    style: dict[str, Any] | None = None


class DiagramEdge(BaseModel):
    id: str
    source: str
    target: str
    label: str | None = None
    animated: bool = False
    style: dict[str, Any] | None = None


class DiagramPayload(BaseModel):
    nodes: list[DiagramNode] = Field(default_factory=list)
    edges: list[DiagramEdge] = Field(default_factory=list)