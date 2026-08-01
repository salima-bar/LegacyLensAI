from __future__ import annotations

from app.ai.context_builder import ProjectContext
from app.ai.prompts import (
    get_analysis_principles,
    get_analysis_rules,
    get_architecture_prompt,
    get_documentation_prompt,
    get_final_instruction,
    get_output_examples,
    get_overview_prompt,
    get_recommendation_prompt,
    get_roadmap_prompt,
    get_system_prompt,
)
from app.ai.prompts.prompt_section import PromptSection


class PromptBuilder:
    """
    Builds the final prompt that will be sent to the LLM.

    Responsibilities
    ----------------
    1. Load prompt sections.
    2. Assemble the final prompt.
    3. Inject the project context.
    4. Inject the expected output schema.
    """

    def __init__(self) -> None:
        """
        Initialize the prompt builder.

        Prompt sections are loaded once during construction
        because they are static and reused for every analysis.
        """

        self.prompt_sections: tuple[PromptSection, ...] = tuple(
            self._load_sections()
        )

    def _load_sections(
        self,
    ) -> list[PromptSection]:
        """
        Load every prompt section used during analysis.
        """

        sections = [

            get_system_prompt(),

            get_analysis_principles(),

            get_analysis_rules(),

            get_overview_prompt(),

            get_architecture_prompt(),

            get_documentation_prompt(),

            get_roadmap_prompt(),

            get_recommendation_prompt(),

            get_output_examples(),

            get_final_instruction(),

        ]

        sections.sort(
            key=lambda section: section.order
        )

        return sections


    def build(
        self,
        context: ProjectContext,
        schema: str,
    ) -> str:
        """
        Build the complete prompt that will be sent
        to the language model.
        """

        lines: list[str] = []

        # Prompt sections
        lines.extend(
            self._build_sections()
        )

        # Project context
        self._append_context(
            lines,
            context,
        )

        # Expected output schema
        self._append_schema(
            lines,
            schema,
        )

        return "\n".join(lines)

    def _build_sections(
        self,
    ) -> list[str]:
        """
        Merge every prompt section into one list.
        """

        lines: list[str] = []

        for section in self.prompt_sections:

            lines.append(
                f"# {section.title}"
            )

            lines.append("")

            lines.append(
                section.content.strip()
            )

            lines.append("")
            lines.append("")

        return lines

    def _append_context(
        self,
        lines: list[str],
        context: ProjectContext,
    ) -> None:
        """
        Append the prepared project context.
        """

        lines.append("# Project Context")

        lines.append("")

        lines.append(
            context.content.strip()
        )

        lines.append("")
        lines.append("")

    def _append_schema(
        self,
        lines: list[str],
        schema: str,
    ) -> None:
        """
        Append the expected JSON schema.
        """

        lines.append("# Expected Output Schema")

        lines.append("")

        lines.append(schema)

        lines.append("")

    def reload(self) -> None:
        """
        Reload every prompt section.

        Useful during development if prompt definitions
        are modified without recreating the PromptBuilder.
        """

        self.sections = tuple(
            self._load_sections()
        )

    def section_titles(
        self,
    ) -> list[str]:
        """
        Return the ordered prompt section titles.

        Mainly intended for debugging or testing.
        """

        return [
            section.title
            for section in self.sections
        ]