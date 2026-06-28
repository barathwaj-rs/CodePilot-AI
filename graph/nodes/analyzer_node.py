from graph.state import CodePilotState

from services.repository.analyzer import RepositoryAnalyzer
from services.logger.workflow_logger import WorkflowLogger


def analyzer_node(
    state: CodePilotState,
) -> CodePilotState:
    """
    Analyze the repository and store the results
    in the workflow state.
    """

    WorkflowLogger.log(
        state,
        "🔍 Analyzing repository...",
    )

    analysis = RepositoryAnalyzer.analyze(
        state["repo_url"]
    )

    state["repo_analysis"] = analysis

    WorkflowLogger.log(
        state,
        "✅ Repository analysis completed.",
    )

    return state