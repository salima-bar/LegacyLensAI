from __future__ import annotations

import json

from app.ai.llm import LLMResponse
from app.ai.result import AnalysisResult
from pydantic import ValidationError


class ParserError(Exception):
    """Base exception for parser-related errors."""
    pass


class InvalidJSONError(ParserError):
    """Raised when the response does not contain valid JSON."""
    pass


class InvalidSchemaError(ParserError):
    """Raised when the JSON structure is invalid."""
    pass


class AnalysisParser:
    """
    Converts LLM responses into validated AnalysisResult objects.

    Responsibilities
    ----------------
    1. Extract JSON from the LLM response.
    2. Validate the JSON structure.
    3. Convert JSON into AnalysisResult.
    """

    def __init__(self) -> None:
        """Initialize the parser."""
        pass

    def parse(
        self,
        response: LLMResponse,
    ) -> AnalysisResult:
        """
        Parse an LLM response into a validated AnalysisResult.

        Parameters
        ----------
        response:
            The normalized response returned by the language model.

        Returns
        -------
        AnalysisResult
            The validated analysis result.

        Raises
        ------
        ParserError
            If the response cannot be parsed.
        """

        json_data = self._extract_json(
            response.text,
        )

        return self._build_result(
            json_data,
        )    

    def _extract_json(
        self,
        text: str,
    ) -> dict[str, object]:
        """
        Extract and deserialize JSON from the LLM response.

        Parameters
        ----------
        text:
            Raw text returned by the language model.

        Returns
        -------
        dict
            Parsed JSON object.

        Raises
        ------
        InvalidJSONError
            If the response is not valid JSON.
        """

        try:
            return json.loads(text)

        except json.JSONDecodeError as exc:
            raise InvalidJSONError(
                "The language model did not return valid JSON."
            ) from exc


    def _build_result(
        self,
        json_data: dict[str, object],
    ) -> AnalysisResult:
        """
        Build an AnalysisResult from parsed JSON.

        Parameters
        ----------
        json_data:
            Parsed JSON dictionary.

        Returns
        -------
        AnalysisResult
            Validated analysis result.

        Raises
        ------
        InvalidSchemaError
            If the JSON structure does not match the expected schema.
        """

        try:
            return AnalysisResult.model_validate(
                json_data,
            )

        except ValidationError as exc:
            raise InvalidSchemaError(
                "The analysis result does not match the expected schema."
            ) from exc