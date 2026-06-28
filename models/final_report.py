from dataclasses import dataclass, field

from models.review_result import ReviewIssue


@dataclass
class FinalReport:
    """
    Final workflow result returned to the user.
    """

    success: bool

    task: str

    retries: int

    summary: str

    generated_files: list[str] = field(default_factory=list)

    issues: list[ReviewIssue] = field(default_factory=list)