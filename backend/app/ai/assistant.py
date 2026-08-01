from __future__ import annotations

from app.ai.llm import LLMClient
from app.ai.prompts.assistant_prompt import get_assistant_prompt
from app.ai.result import (
    AnalysisResult,
    AssistantResponse,
    ConversationHistory,
)


class ProjectAssistantError(Exception):
    """
    Raised when the assistant workflow fails.
    """
    pass


class ProjectAssistant:
    """
    AI assistant specialized in answering questions
    about an already analyzed project.

    Responsibilities
    ----------------
    1. Build the assistant prompt.
    2. Send the prompt to the language model.
    3. Return the assistant response.
    """

    def __init__(
        self,
        llm: LLMClient,
    ) -> None:
        self._llm = llm


    def chat(
        self,
        analysis: AnalysisResult,
        history: ConversationHistory,
        message: str,
    ) -> AssistantResponse:
        """
        Generate an AI assistant response.

        Parameters
        ----------
        analysis:
            Analysis result of the current project.

        history:
            Previous conversation with the assistant.

        message:
            Latest user message.

        Returns
        -------
        AssistantResponse
            Assistant reply.
        """

        try:

            prompt = get_assistant_prompt(
                analysis=analysis,
                history=history,
                message=message,
            )

            response = self._llm.generate(
                prompt.to_prompt(),
            )

            return AssistantResponse(
                answer=response.text,
            )

        except Exception as exc:
            raise ProjectAssistantError(
                "Failed to generate assistant response."
            ) from exc
