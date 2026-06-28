from dataclasses import dataclass, field


@dataclass
class ReviewIssue:
    """
    Represents one issue found during review.
    """

    severity: str
    file: str
    description: str


@dataclass
class ReviewResult:
    """
    Output produced by the Reviewer Agent.
    """

    approved: bool

    summary: str

    issues: list[ReviewIssue] = field(default_factory=list)