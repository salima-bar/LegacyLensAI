from __future__ import annotations

from app.ai.context_builder import ContextBuilder
from app.ai.llm import LLMClient
from app.ai.parser import AnalysisParser
from app.ai.prompt_builder import PromptBuilder
from app.ai.result import (
    AnalysisResult,
    ProjectFiles,
)


class AnalysisEngineError(Exception):
    """Raised when the analysis workflow fails."""


class AnalysisEngine:
    """
    Coordinates the complete AI analysis workflow.

    Workflow
    --------
    1. Build the project context.
    2. Build the analysis prompt.
    3. Send the prompt to the language model.
    4. Parse the response.
    5. Return the validated analysis result.
    """

    def __init__(
        self,
        context_builder: ContextBuilder,
        prompt_builder: PromptBuilder,
        llm: LLMClient,
        parser: AnalysisParser,
    ) -> None:
        self._context_builder = context_builder
        self._prompt_builder = prompt_builder
        self._llm = llm
        self._parser = parser

    def analyze_project(
        self,
        project: ProjectFiles,
    ) -> AnalysisResult:
        """
        Run a complete AI analysis.

        Parameters
        ----------
        project:
            Project files prepared for analysis.

        Returns
        -------
        AnalysisResult
            Validated analysis result.
        """

        try:
            context = self._context_builder.build(project)

            prompt = self._prompt_builder.build(context)

            response = self._llm.generate(prompt)

            return self._parser.parse(response)

        except Exception as exc:
            raise AnalysisEngineError(
                "Failed to complete the analysis workflow."
            ) from exc
        
      

