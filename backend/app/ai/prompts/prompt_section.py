from __future__ import annotations

from pydantic import BaseModel, Field


class PromptSection(BaseModel):
    """
    Represents a single section of the final prompt.
    """

    order: int = Field(
        description="Section order inside the final prompt.",
    )

    title: str = Field(
        description="Prompt section title.",
    )

    content: str = Field(
        description="Prompt section content.",
    )

    def to_prompt(self) -> str:
        """
        Convert this section into formatted prompt text.
        """

        return (
            f"# {self.title}\n\n"
            f"{self.content.strip()}"
        )