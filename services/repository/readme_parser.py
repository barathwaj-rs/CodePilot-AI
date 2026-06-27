from pathlib import Path


class ReadmeParser:
    """
    Reads the repository README file.
    """

    README_FILES = [
        "README.md",
        "readme.md",
        "README.txt",
    ]

    @staticmethod
    def parse(repo_path: str) -> str:

        root = Path(repo_path)

        for filename in ReadmeParser.README_FILES:

            path = root / filename

            if path.exists():

                return path.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )

        return ""