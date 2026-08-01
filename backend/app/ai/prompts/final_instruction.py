from __future__ import annotations

from app.ai.prompts.prompt_section import PromptSection


def get_final_instruction() -> PromptSection:
    """
    Returns the final mandatory instructions that the AI
    must follow before generating its response.
    """

    return PromptSection(
        order=100,
        title="Final Instructions",
        content="""
Carefully review all previous instructions before generating the response.

Your response must satisfy all of the following requirements:

- Return exactly one valid JSON object.
- Follow the provided schema exactly.
- Do not omit required fields.
- Do not invent information.
- Base every conclusion on evidence found in the uploaded project.
- Keep all sections internally consistent.
- Use enum values exactly as provided by the schema.
- Use empty arrays instead of null whenever appropriate.
- Use empty objects instead of null whenever required.
- If information cannot be determined, explicitly state that it is unknown.
- Do not include Markdown.
- Do not include explanations outside the JSON object.
- Do not include comments.
- Do not include code fences.

Before returning the response, perform one final validation to ensure that:

- The JSON is syntactically valid.
- Every required field is present.
- All field types match the schema.
- All recommendations are technically justified.
- No duplicated recommendations exist.
- No contradictory statements exist between sections.

Return only the final JSON object.
""",
    )