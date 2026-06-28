from graph.state import CodePilotState
from services.repository.analyzer import RepositoryAnalyzer


def analyzer_node(
    state: CodePilotState,
) -> CodePilotState:
    """
    Analyze the repository and store the results
    in the workflow state.
    """

    analysis = RepositoryAnalyzer.analyze(
        state["repo_url"]
    )

    state["repo_analysis"] = analysis

    return state