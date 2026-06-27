from pathlib import Path


class FrameworkDetector:
    """
    Detect frameworks used in the repository.
    """

    @staticmethod
    def detect(repo_path: str, files: list[str]) -> list[str]:

        frameworks = []

        root = Path(repo_path)

        # ---------- Python ----------

        if "requirements.txt" in files:

            content = (root / "requirements.txt").read_text(
                encoding="utf-8",
                errors="ignore"
            ).lower()

            if "fastapi" in content:
                frameworks.append("FastAPI")

            if "django" in content:
                frameworks.append("Django")

            if "flask" in content:
                frameworks.append("Flask")

            if "sqlalchemy" in content:
                frameworks.append("SQLAlchemy")

        # ---------- pyproject ----------

        if "pyproject.toml" in files:

            content = (root / "pyproject.toml").read_text(
                encoding="utf-8",
                errors="ignore"
            ).lower()

            if "fastapi" in content:
                frameworks.append("FastAPI")

            if "langgraph" in content:
                frameworks.append("LangGraph")

            if "gradio" in content:
                frameworks.append("Gradio")

        # Remove duplicates

        return sorted(set(frameworks))