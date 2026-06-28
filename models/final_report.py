from dataclasses import dataclass, field

from models.review_result import ReviewIssue


@dataclass
class FinalReport:
    """
    Final execution report produced by CodePilot AI.
    """

    success: bool

    task: str

    retries: int

    summary: str

    generated_files: list[str] = field(default_factory=list)

    issues: list[ReviewIssue] = field(default_factory=list)

    # Git Information
    git_branch: str = ""

    git_commit: str = ""

    commit_message: str = ""