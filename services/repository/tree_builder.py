from pathlib import Path


class TreeBuilder:
    """
    Builds a filtered list of repository files.
    """

    IGNORE_DIRS = {
        ".git",
        ".venv",
        "__pycache__",
        "node_modules",
        ".idea",
        ".vscode",
        ".pytest_cache",
        "dist",
        "build",
    }

    @staticmethod
    def build(repo_path: str) -> list[str]:
        """
        Scan the repository and return relative file paths.
        """

        root = Path(repo_path)

        files = []

        for path in root.rglob("*"):

            if any(part in TreeBuilder.IGNORE_DIRS for part in path.parts):
                continue

            if path.is_file():
                files.append(
                  path.relative_to(root).as_posix()
                )

        files.sort()

        return files