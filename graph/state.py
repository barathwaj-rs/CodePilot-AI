from typing import TypedDict

from models.repository_analysis import RepositoryAnalysis
from models.repository_context import RepositoryContext
from models.execution_plan import ExecutionPlan


class CodePilotState(TypedDict):
    """
    Shared state used by the LangGraph workflow.
    """

    # User Input
    repo_url: str
    user_task: str

    # Repository
    repo_analysis: RepositoryAnalysis
    repository_context: RepositoryContext

    # AI Planning
    execution_plan: ExecutionPlan | None

    # Future
    generated_code: str | None
    review_report: str | None
    final_response: str | None