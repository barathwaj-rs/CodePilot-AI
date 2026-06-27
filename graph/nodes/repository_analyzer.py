from graph.state import CodePilotState
from services.repository.analyzer import RepositoryAnalyzer


def repository_analyzer(state: CodePilotState) -> CodePilotState:

    print("Repository Analyzer Node")

    # For now, analyze our current project.
    # Later this will use the cloned repository path.
    repo_path = "."

    analysis = RepositoryAnalyzer.analyze(repo_path)

    state["repo_analysis"] = analysis

    return state