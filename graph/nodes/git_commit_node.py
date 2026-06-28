from graph.state import CodePilotState

from services.git.git_service import GitService


def git_commit_node(
    state: CodePilotState,
) -> CodePilotState:
    """
    Commit staged changes.
    """

    commit_hash = GitService.commit(
        repository_path=state["repo_url"],
        message=state["commit_message"],
    )

    state["git_commit"] = commit_hash

    print()
    print("=" * 60)
    print("GIT COMMIT")
    print("=" * 60)
    print(commit_hash)

    return state