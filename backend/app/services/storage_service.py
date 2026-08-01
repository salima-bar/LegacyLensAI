from __future__ import annotations

import shutil
import uuid
import zipfile
from pathlib import Path

from app.ai.result import (
    ProjectFile,
    ProjectFiles,
)
from app.constants.files import (
    IGNORED_DIRECTORIES,
    IGNORED_EXTENSIONS,
)
from fastapi import UploadFile

"""
Storage Service

Responsible for:

1. Saving uploaded projects.
2. Extracting ZIP archives.
3. Reading project files.
4. Deleting stored projects.

This service DOES NOT interact with:
- Database
- AI
- CRUD
"""


# ==========================================================
# PUBLIC FUNCTIONS
# ==========================================================

def save_uploaded_project(
    uploaded_file,
) -> str:
    """
    Save uploaded ZIP file and extract it.

    Returns:
        Storage path of the extracted project.
    """

    project_directory = _create_project_directory()

    zip_path = _save_zip_file(
        uploaded_file=uploaded_file,
        project_directory=project_directory,
    )

    _extract_zip(
        zip_path=zip_path,
        destination=project_directory,
    )

    return str(project_directory)


def read_project_files(
    storage_path: str,
    project_name: str,
) -> ProjectFiles:
    """
    Read all project files from storage.

    Returns:
        ProjectFiles ready for AI analysis.
    """

    project_directory = Path(storage_path)

    return _collect_project_files(
        project_directory=project_directory,
        project_name=project_name,
    )


def delete_project_files(
    storage_path: str,
) -> None:
    """
    Delete an uploaded project.
    """

    _delete_directory(
        directory=Path(storage_path),
    )


# ==========================================================
# PRIVATE FUNCTIONS
# ==========================================================

def _create_project_directory() -> Path:
    """
    Create a directory for a newly uploaded project.

    Returns:
        Path to the created project directory.
    """

    uploads_directory = Path("uploads")

    uploads_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    project_directory = uploads_directory / str(
        uuid.uuid4(),
    )

    project_directory.mkdir()

    return project_directory


def _save_zip_file(
    uploaded_file: UploadFile,
    project_directory: Path,
) -> Path:
    """
    Save the uploaded ZIP archive.

    Returns:
        Path to the saved ZIP file.
    """

    zip_path = project_directory / "project.zip"

    with zip_path.open("wb") as buffer:
        shutil.copyfileobj(
            uploaded_file.file,
            buffer,
        )

    return zip_path


def _extract_zip(
    zip_path: Path,
    destination: Path,
) -> None:
    """
    Extract the uploaded ZIP archive.

    Parameters
    ----------
    zip_path:
        Path to the uploaded ZIP file.

    destination:
        Directory where the archive will be extracted.
    """

    if not zipfile.is_zipfile(
        zip_path,
    ):
        raise ValueError(
            "Uploaded file is not a valid ZIP archive.",
        )
    
    with zipfile.ZipFile(
        zip_path,
    "r",
    ) as archive:

        destination = destination.resolve()

        for member in archive.infolist():

            target_path = (
                destination / member.filename
            ).resolve()

            if not str(target_path).startswith(
                str(destination)
            ):
                raise ValueError(
                    "Unsafe ZIP archive detected."
                )

            archive.extract(
                member,
                destination,
            )


def _collect_project_files(
    project_directory: Path,
    project_name: str,
) -> ProjectFiles:
    """
    Read all supported project files.

    Returns:
        ProjectFiles ready for AI analysis.
    """

    files: list[Path] = []

    for path in project_directory.rglob("*"):

        if not path.is_file():
            continue

        if any(
            part in IGNORED_DIRECTORIES
            for part in path.parts
        ):
            continue

        files.append(path)

    project_files: list[ProjectFile] = []

    for path in files:

        if path.suffix.lower() in IGNORED_EXTENSIONS:
            continue

        try:

            content = path.read_text(
                encoding="utf-8",
            )

        except UnicodeDecodeError:
            continue

        relative_path = path.relative_to(
            project_directory,
        )

        project_files.append(
            ProjectFile(
                path=str(relative_path),
                content=content,
            )
        )
    return ProjectFiles(
        project_name=project_name,
        root_path=str(project_directory),
        files=project_files,
    )


def _delete_directory(
    directory: Path,
) -> None:
    """
    Delete project directory.
    """

    if directory.exists():
        shutil.rmtree(directory)