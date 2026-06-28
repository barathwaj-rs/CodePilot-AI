from pathlib import Path

from graph.state import CodePilotState
from services.indexing.code_indexer import CodeIndexer


def indexer_node(
    state: CodePilotState,
) -> CodePilotState:
    """
    Build the ChromaDB index for the repository.
    """

    repository_name = Path(
        state["repo_url"]
    ).resolve().name

    indexer = CodeIndexer(
        repository_name=repository_name,
    )

    indexer.index_repository(
        state["repo_url"],
    )

    return state