from dataclasses import dataclass, field


@dataclass
class RepositoryAnalysis:
    """
    Stores all information discovered about a repository.
    """

    files: list[str] = field(default_factory=list)

    languages: dict[str, int] = field(default_factory=dict)

    frameworks: list[str] = field(default_factory=list)

    dependencies: dict[str, list[str]] = field(default_factory=dict)

    entry_points: list[str] = field(default_factory=list)

    readme_summary: str = ""

    git_info: dict = field(default_factory=dict)