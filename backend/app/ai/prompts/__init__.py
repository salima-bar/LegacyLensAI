"""
Public interface for AI prompt sections.

This module re-exports all prompt section factory functions so they
can be imported from a single location.
"""

from .analysis_principles import get_analysis_principles
from .analysis_prompt import (
    get_architecture_prompt,
    get_documentation_prompt,
    get_overview_prompt,
    get_recommendation_prompt,
    get_roadmap_prompt,
)
from .analysis_rules import get_analysis_rules
from .assistant_prompt import get_assistant_prompt
from .final_instruction import get_final_instruction
from .output_examples import get_output_examples
from .system_prompt import get_system_prompt

__all__ = [
    "get_analysis_principles",
    "get_analysis_rules",
    "get_architect_prompt",
    "get_architecture_prompt",
    "get_assistant_prompt",
    "get_documentation_prompt",
    "get_final_instruction",
    "get_output_examples",
    "get_overview_prompt",
    "get_recommendation_prompt",
    "get_roadmap_prompt",
    "get_system_prompt",
]