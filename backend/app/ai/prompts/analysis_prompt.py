from __future__ import annotations

from app.ai.prompts.prompt_section import PromptSection


def get_overview_prompt() -> PromptSection:
    """
    Returns the prompt section responsible for generating
    the project overview.
    """

    return PromptSection(
        order=40,
        title="Project Overview",
        content="""
Objective

Understand the uploaded software project and produce a concise,
accurate overview of the system.

Focus

Focus on understanding what the project is, what it does,
its technical stack, and its overall purpose.

Tasks

- Identify the project purpose.
- Identify the application domain.
- Identify the software type.
- Detect programming languages.
- Detect frameworks.
- Detect major technologies.
- Summarize the overall project.

Expected Result

A concise and technically accurate overview describing
the project and its technology stack.
""",
    )


def get_architecture_prompt() -> PromptSection:
    """
    Returns the prompt section responsible for architecture analysis.
    """

    return PromptSection(
        order=50,
        title="Architecture Analysis",
        content="""
Objective

Analyze the internal architecture of the project.

Focus

Understand how the system is organized rather than
simply describing folders.

Tasks

- Identify architectural layers.
- Identify major components.
- Detect dependencies.
- Detect architectural patterns.
- Identify strengths.
- Identify weaknesses.

Expected Result

A clear architectural analysis describing the project
structure, relationships between components,
and architectural quality.
""",
    )


def get_documentation_prompt() -> PromptSection:
    """
    Returns the prompt section responsible for generating
    technical documentation.
    """

    return PromptSection(
        order=60,
        title="Technical Documentation",
        content="""
Objective

Generate clear technical documentation for the project.

Focus

Explain the project from a software engineer's perspective.

Tasks

- Describe the project.
- Describe important modules.
- Describe the system organization.
- Explain major responsibilities.
- Explain component interactions.

Expected Result

Well-structured technical documentation that helps
developers understand the project.
""",
    )


def get_roadmap_prompt() -> PromptSection:
    """
    Returns the prompt section responsible for creating
    the modernization roadmap.
    """

    return PromptSection(
        order=70,
        title="Modernization Roadmap",
        content="""
Objective

Create a realistic modernization roadmap.

Focus

Prioritize improvements that provide the highest value
while minimizing unnecessary risk.

Tasks

- Identify modernization phases.
- Organize improvements by priority.
- Suggest logical implementation order.
- Consider technical dependencies.
- Consider migration risks.

Expected Result

A phased roadmap describing how the project can
be modernized progressively.
""",
    )


def get_recommendation_prompt() -> PromptSection:
    """
    Returns the prompt section responsible for generating
    technical recommendations.
    """

    return PromptSection(
        order=80,
        title="Technical Recommendations",
        content="""
Objective

Generate useful recommendations for improving the project.

Focus

Provide practical recommendations that developers
can realistically implement.

Tasks

- Identify code quality improvements.
- Identify architectural improvements.
- Identify security improvements.
- Identify performance improvements.
- Identify documentation improvements.
- Prioritize recommendations.

Expected Result

A list of specific, technically justified,
actionable recommendations.
""",
    )