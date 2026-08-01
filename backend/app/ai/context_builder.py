from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from enum import Enum, IntEnum
from pathlib import Path

from app.ai.result import (
    ProjectContext,
    ProjectFile,
    ProjectFiles,
)
from app.constants.files import (
    CONFIGURATION_EXTENSION_TYPES,
    CONFIGURATION_FILES,
    CONFIGURATION_TYPES,
    DOCUMENTATION_FILES,
    DOCUMENTATION_TYPES,
    ENTRY_POINT_FILES,
    IGNORED_DIRECTORIES,
    IGNORED_EXTENSIONS,
    SOURCE_TYPES,
)

# ==========================================================
# CONTEXT LIMITS
# ==========================================================

MAX_FILE_CHARACTERS = 12_000

TRUNCATION_NOTICE = """

------------------------------
Content truncated
------------------------------

The middle part of this file was omitted because it exceeds
the maximum allowed size for AI analysis.

"""

# ==========================================================
# FILE CATEGORY
# ==========================================================

class FileCategory(str, Enum):
    CONFIGURATION = "Configuration Files"
    DOCUMENTATION = "Documentation"
    ENTRY_POINT = "Entry Points"
    SOURCE_CODE = "Source Code"
    OTHER = "Other Files"


# ==========================================================
# FILE PRIORITY
# ==========================================================

class FilePriority(IntEnum):
    VERY_HIGH = 1
    HIGH = 2
    MEDIUM = 3
    LOW = 4
    VERY_LOW = 5


# ==========================================================
# CONTEXT FILE
# ==========================================================


@dataclass(slots=True)
class ContextFile:
    """
    Represents one project file after preprocessing.

    This object stores both the original file and the metadata
    required to build the final project context.
    """

    file: ProjectFile

    category: FileCategory

    file_type: str

    priority: FilePriority


# ==========================================================
# CONTEXT BUILDER
# ==========================================================


class ContextBuilder:
    """
    Builds a structured project context that will later
    be injected into the final LLM prompt.

    Responsibilities
    ----------------
    1. Remove unnecessary files.
    2. Categorize project files.
    3. Sort files by importance.
    4. Build a clean textual context.
    """

    def build(
        self,
        project: ProjectFiles,
    ) -> ProjectContext:
        """
        Build the complete project context.
        """

        files = self._filter_files(project.files)

        context_files = self._categorize_files(files)

        context_files = self._sort_files(context_files)

        context = self._build_context(
            project.project_name,
            context_files,
        )

        return ProjectContext(
            project_name=project.project_name,
            content=context,
        )

    def _filter_files(
        self,
        files: list[ProjectFile],
    ) -> list[ProjectFile]:
        """
        Remove files that should not be analyzed.

        Examples:
        - Cache directories
        - Build artifacts
        - Binary files
        - Empty files
        """

        filtered: list[ProjectFile] = []

        for file in files:

            path = Path(file.path)

            # Ignore directories
            if any(
                part in IGNORED_DIRECTORIES
                for part in path.parts
            ):
                continue

            # Ignore file extensions
            if path.suffix.lower() in IGNORED_EXTENSIONS:
                continue

            # Ignore empty files
            if not file.content.strip():
                continue

            filtered.append(file)

        return filtered


# ==========================================================
# FILE CATEGORIZATION
# ==========================================================

    def _categorize_files(
        self,
        files: list[ProjectFile],
    ) -> list[ContextFile]:
        """
        Convert ProjectFile objects into ContextFile objects
        enriched with category and file type information.
        """

        context_files: list[ContextFile] = []

        for file in files:

            context_files.append(
                ContextFile(
                    file=file,
                    category=self._detect_category(file),
                    file_type=self._detect_file_type(file),
                    priority=self._detect_priority(file),
                )
            )

        return context_files

    def _detect_category(
        self,
        file: ProjectFile,
    ) -> FileCategory:
        """
        Detect the high-level category of a project file.
        """

        path = Path(file.path)

        filename = path.name

        suffix = path.suffix.lower()

        # Documentation
        if (
            suffix == ".md"
            or filename in DOCUMENTATION_FILES
        ):
            return FileCategory.DOCUMENTATION

        # Entry points
        if filename in ENTRY_POINT_FILES:
            return FileCategory.ENTRY_POINT

        # Configuration
        if (
            filename in CONFIGURATION_FILES
            or suffix in CONFIGURATION_EXTENSION_TYPES
        ):
            return FileCategory.CONFIGURATION

        # Source code
        if suffix in SOURCE_TYPES:
            return FileCategory.SOURCE_CODE

        return FileCategory.OTHER

    def _detect_file_type(
        self,
        file: ProjectFile,
    ) -> str:
        """
        Return a human-readable description of the file type.
        """

        path = Path(file.path)

        filename = path.name

        suffix = path.suffix.lower()

        # Documentation
        if filename in DOCUMENTATION_TYPES:
            return DOCUMENTATION_TYPES[filename]

        # Configuration
        if filename in CONFIGURATION_TYPES:
            return CONFIGURATION_TYPES[filename]

        # Source code
        if suffix in SOURCE_TYPES:
            return SOURCE_TYPES[suffix]

        # Configuration extensions
        if suffix in CONFIGURATION_EXTENSION_TYPES:
            return CONFIGURATION_EXTENSION_TYPES[suffix]

        # Generic markdown
        if suffix == ".md":
            return "Markdown Documentation"

        return "Project File"


    def _detect_priority(
        self,
        file: ProjectFile,
    ) -> FilePriority:
        """
        Assign a priority that determines the order in which
        files are presented to the LLM.
        """

        filename = Path(file.path).name

        # Highest priority
        if (
            filename in DOCUMENTATION_FILES
            or filename in CONFIGURATION_FILES
            or filename in ENTRY_POINT_FILES
        ):
            return FilePriority.VERY_HIGH

        suffix = Path(file.path).suffix.lower()

        if suffix in SOURCE_TYPES:
            return FilePriority.HIGH

        if suffix in CONFIGURATION_EXTENSION_TYPES:
            return FilePriority.MEDIUM

        if suffix == ".md":
            return FilePriority.MEDIUM

        return FilePriority.LOW

# ==========================================================
# CONTEXT GENERATION
# ==========================================================

    def _sort_files(
        self,
        files: list[ContextFile],
    ) -> list[ContextFile]:
        """
        Sort files by priority first,
        then alphabetically.
        """

        return sorted(
            files,
            key=lambda file: (
                file.priority,
                file.file.path.lower(),
            ),
        )

    def _group_files(
        self,
        files: list[ContextFile],
    ) -> dict[FileCategory, list[ContextFile]]:
        """
        Group files by category.
        """

        grouped: defaultdict[
            FileCategory,
            list[ContextFile],
        ] = defaultdict(list)

        for file in files:
            grouped[file.category].append(file)

        return dict(grouped)


    def _prepare_content(
        self,
        content: str,
    ) -> str:
        """
        Prepare file content before sending it to the LLM.
        Large files are truncated while preserving both
        the beginning and the end of the file.
        """

        content = content.strip()

        if len(content) <= MAX_FILE_CHARACTERS:
            return content

        half = MAX_FILE_CHARACTERS // 2

        beginning = content[:half]

        ending = content[-half:]

        return (
            beginning
            + TRUNCATION_NOTICE
            + ending
        )

    def _format_file(
        self,
        file: ContextFile,
    ) -> list[str]:
        """
        Format one file inside the final context.
        """

        return [

            "========================================",

            f"Path: {file.file.path}",

            f"Category: {file.category.value}",

            f"Type: {file.file_type}",

            "",

            "Content:",

            self._prepare_content(
                file.file.content,
            ),

            "",

        ]


    def _build_context(
        self,
        project_name: str,
        files: list[ContextFile],
    ) -> str:
        """
        Build the final project context.
        """

        grouped = self._group_files(files)

        lines: list[str] = []

        lines.append("# Project")
        lines.append("")
        lines.append(f"Name: {project_name}")
        lines.append(f"Files Included: {len(files)}")
        lines.append("")

        ordered_categories = [

            FileCategory.CONFIGURATION,

            FileCategory.DOCUMENTATION,

            FileCategory.ENTRY_POINT,

            FileCategory.SOURCE_CODE,

            FileCategory.OTHER,

        ]

        for category in ordered_categories:

            category_files = grouped.get(category)

            if not category_files:
                continue

            lines.append(f"# {category.value}")
            lines.append("")

            for file in category_files:

                lines.extend(
                    self._format_file(file)
                )

            lines.append("")

        return "\n".join(lines)