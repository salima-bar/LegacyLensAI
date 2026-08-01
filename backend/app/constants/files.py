from __future__ import annotations

# ==========================================================
# DIRECTORIES TO IGNORE
# ==========================================================

IGNORED_DIRECTORIES = {
    ".git",
    ".github",
    ".idea",
    ".vscode",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".venv",
    "venv",
    "env",
    "node_modules",
    "dist",
    "build",
    "target",
    "bin",
    "obj",
}

# ==========================================================
# FILE EXTENSIONS TO IGNORE
# ==========================================================

IGNORED_EXTENSIONS = {
    ".pyc",
    ".pyo",
    ".class",
    ".dll",
    ".exe",
    ".so",
    ".dylib",
    ".jar",
    ".zip",
    ".tar",
    ".gz",
    ".7z",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".bmp",
    ".ico",
    ".svg",
    ".mp3",
    ".mp4",
    ".avi",
    ".mov",
    ".pdf",
}

# ==========================================================
# IMPORTANT FILES
# ==========================================================

DOCUMENTATION_FILES = {
    "README.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "LICENSE.txt",
}

CONFIGURATION_FILES = {
    "requirements.txt",
    "pyproject.toml",
    "setup.py",
    "package.json",
    "pom.xml",
    "build.gradle",
    "Dockerfile",
    "docker-compose.yml",
    ".env.example",
}

ENTRY_POINT_FILES = {
    "main.py",
    "app.py",
    "run.py",
    "manage.py",
    "Program.cs",
    "Main.java",
    "index.js",
    "index.ts",
    "server.js",
    "server.ts",
}

# ==========================================================
# FILE TYPE MAPPINGS
# ==========================================================

DOCUMENTATION_TYPES = {
    "README.md": "Project Documentation",
    "CHANGELOG.md": "Project Changelog",
    "CONTRIBUTING.md": "Contribution Guide",
    "LICENSE": "License",
    "LICENSE.txt": "License",
}

CONFIGURATION_TYPES = {
    "Dockerfile": "Docker Configuration",
    "docker-compose.yml": "Docker Compose Configuration",
    "requirements.txt": "Python Dependencies",
    "pyproject.toml": "Python Project Configuration",
    "package.json": "Node Project Configuration",
    "pom.xml": "Maven Configuration",
    "build.gradle": "Gradle Configuration",
    ".env.example": "Environment Template",
}

SOURCE_TYPES = {
    ".py": "Python Source",
    ".java": "Java Source",
    ".cs": "C# Source",
    ".js": "JavaScript Source",
    ".ts": "TypeScript Source",
    ".tsx": "TypeScript React Source",
    ".jsx": "JavaScript React Source",
    ".cpp": "C++ Source",
    ".c": "C Source",
    ".go": "Go Source",
    ".php": "PHP Source",
    ".rb": "Ruby Source",
    ".kt": "Kotlin Source",
    ".swift": "Swift Source",
    ".rs": "Rust Source",
}

CONFIGURATION_EXTENSION_TYPES = {
    ".json": "JSON Configuration",
    ".yaml": "YAML Configuration",
    ".yml": "YAML Configuration",
    ".toml": "TOML Configuration",
    ".xml": "XML Configuration",
    ".ini": "INI Configuration",
    ".cfg": "Configuration File",
    ".conf": "Configuration File",
    ".properties": "Properties Configuration",
}