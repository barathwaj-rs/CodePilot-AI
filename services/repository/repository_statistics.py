from pathlib import Path


class RepositoryStatistics:
    """
    Calculates repository statistics.
    """

    @staticmethod
    def analyze(files: list[str]) -> dict:

        python_files = 0
        markdown_files = 0
        other_files = 0

        for file in files:

            suffix = Path(file).suffix.lower()

            if suffix == ".py":
                python_files += 1

            elif suffix == ".md":
                markdown_files += 1

            else:
                other_files += 1

        return {
            "total_files": len(files),
            "python_files": python_files,
            "markdown_files": markdown_files,
            "other_files": other_files,
        }