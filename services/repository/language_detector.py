from pathlib import Path


class LanguageDetector:
    """
    Detect programming languages from file extensions.
    """

    EXTENSION_MAP = {
        ".py": "Python",
        ".js": "JavaScript",
        ".jsx": "JavaScript",
        ".ts": "TypeScript",
        ".tsx": "TypeScript",
        ".java": "Java",
        ".cpp": "C++",
        ".c": "C",
        ".cs": "C#",
        ".go": "Go",
        ".rs": "Rust",
        ".php": "PHP",
        ".rb": "Ruby",
        ".swift": "Swift",
        ".kt": "Kotlin",
        ".html": "HTML",
        ".css": "CSS",
        ".scss": "SCSS",
        ".json": "JSON",
        ".yaml": "YAML",
        ".yml": "YAML",
        ".xml": "XML",
        ".md": "Markdown",
        ".sql": "SQL",
        ".sh": "Shell",
    }

    @staticmethod
    def detect(files: list[str]) -> dict[str, int]:

        languages = {}

        for file in files:

            extension = Path(file).suffix.lower()

            language = LanguageDetector.EXTENSION_MAP.get(extension)

            if language is None:
                continue

            languages[language] = languages.get(language, 0) + 1

        return dict(sorted(languages.items()))