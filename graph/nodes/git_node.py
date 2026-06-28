from graph.state import CodePilotState
from services.git.git_service import GitService


def git_node(
    state: CodePilotState,
) -> CodePilotState:
    """
    Creates and checks out a feature branch
    for the current CodePilot task.
    """

    branch = GitService.create_feature_branch(
        repository_path=state["repo_url"],
        task=state["user_task"],
    )

    state["git_branch"] = branch

    print()
    print("=" * 60)
    print("GIT")
    print("=" * 60)
    print(f"Working Branch: {branch}")

    return state