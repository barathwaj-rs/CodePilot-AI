from pathlib import Path


class EntryPointDetector:
    """
    Detects application entry points.
    """

    ENTRY_POINTS = {
        "main.py",
        "app.py",
        "manage.py",
        "run.py",
        "server.py",
        "__main__.py",
    }

    @staticmethod
    def detect(repo_path: str, files: list[str]) -> list[str]:

        entry_points = []

        for file in files:

            name = Path(file).name

            if name in EntryPointDetector.ENTRY_POINTS:
                entry_points.append(file)

        return sorted(entry_points)