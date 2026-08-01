from __future__ import annotations

from app.ai.prompts.prompt_section import PromptSection


def get_output_examples() -> PromptSection:
    """
    Returns concise examples that illustrate the expected
    quality and style of the generated analysis.

    These examples are not intended to represent the complete
    JSON output. Their purpose is to demonstrate the level of
    detail, technical reasoning, and writing style expected
    from the AI model.
    """

    return PromptSection(
        order=90,
        title="Output Examples",
        content="""
The following examples demonstrate the expected quality of the analysis.


------------------------------------------------------------
Example: Project Summary
------------------------------------------------------------

Good:

"Legacy Java web application used for inventory management.
The project follows a layered architecture with REST APIs,
Spring Boot, PostgreSQL, and Maven."

Bad:

"This is a Java project."


------------------------------------------------------------
Example: Architecture Observation
------------------------------------------------------------

Good:

"The project follows a three-layer architecture consisting of
Presentation, Business Logic, and Persistence layers.
Dependencies flow correctly from Presentation to Business
and finally to Persistence."

Bad:

"The project has several folders."


------------------------------------------------------------
Example: Technical Recommendation
------------------------------------------------------------

Good:

Title:
Replace deprecated authentication library.

Description:
The current authentication library is no longer maintained.
Migrating to Spring Security will improve security and
long-term maintainability.

Priority:
High

Category:
Security

Bad:

"Improve authentication."


------------------------------------------------------------
Example: Modernization Roadmap
------------------------------------------------------------

Good:

Phase 1
- Upgrade project dependencies.
- Remove deprecated libraries.

Phase 2
- Introduce automated testing.
- Refactor authentication module.

Phase 3
- Optimize database performance.
- Improve documentation.

Bad:

"Modernize the project."


------------------------------------------------------------
Example: Evidence-Based Analysis
------------------------------------------------------------

Good:

"The project uses PostgreSQL because the configuration
inside application.properties references a PostgreSQL
database driver."

Bad:

"The project probably uses PostgreSQL."


------------------------------------------------------------
Example: Unknown Information
------------------------------------------------------------

Good:

"The deployment strategy could not be determined from
the uploaded project."

Bad:

"The project is deployed on Kubernetes."
""",
    )