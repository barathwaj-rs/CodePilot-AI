from typing import TypedDict

from models.repository_analysis import RepositoryAnalysis
from models.repository_context import RepositoryContext
from models.execution_plan import ExecutionPlan
from models.generation_result import GenerationResult
from models.review_result import ReviewResult
from models.final_report import FinalReport


class CodePilotState(TypedDict):
    """
    Shared state used by the LangGraph workflow.
    """

    # User Input
    repo_url: str
    user_task: str

    # Repository
    repo_analysis: RepositoryAnalysis | None
    repository_context: RepositoryContext | None

    # AI Planning
    execution_plan: ExecutionPlan | None

    # AI Generation
    generation_result: GenerationResult | None

    # AI Review
    review_result: ReviewResult | None

    retry_count: int
    
    # Git
    git_branch: str | None
    git_commit: str | None
    commit_message: str | None
    # Final Response
    final_report: FinalReport | None

    workflow_logs: list[str]