from graph.state import CodePilotState
from services.git.git_service import GitService


def git_stage_node(
    state: CodePilotState,
) -> CodePilotState:
    """
    Stage all generated files.
    """

    GitService.stage_all(
        state["repo_url"],
    )

    print()
    print("=" * 60)
    print("GIT STAGE")
    print("=" * 60)
    print("All changes staged.")

    return state