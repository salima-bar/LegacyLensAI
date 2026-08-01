from __future__ import annotations

from app.ai.prompts.prompt_section import PromptSection


def get_analysis_rules() -> PromptSection:
    """
    Returns the mandatory rules that the AI must follow
    during project analysis.
    """

    return PromptSection(
        order=30,
        title="Analysis Rules",
        content="""
# Output Rules

- Return exactly one valid JSON object.
- Follow the provided schema exactly.
- Do not generate Markdown.
- Do not generate explanations outside the JSON response.
- Do not include code fences.
- Do not include comments.

# Data Integrity Rules

- Never invent technologies.
- Never invent frameworks.
- Never invent project components.
- Never fabricate architectural layers.
- Never fabricate dependencies.
- Use "unknown" when information cannot be determined.
- Avoid duplicated recommendations.

# Schema Rules

- Respect every field type.
- Respect every enum value.
- Do not omit required fields.
- Return empty lists instead of null whenever appropriate.
- Return empty objects when required by the schema.
- Keep field names exactly as defined.

# Analysis Rules

- Analyze only the uploaded project.
- Ignore binary files.
- Ignore cache folders.
- Ignore generated files when possible.
- Focus on source code and project configuration.
- Base every conclusion on available evidence.

# Recommendation Rules

- Recommendations must be actionable.
- Recommendations must be technically justified.
- Prioritize high-impact improvements.
- Avoid generic advice.
"""
    )