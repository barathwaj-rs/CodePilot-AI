from graph.state import CodePilotState
from services.rag.context_builder import ContextBuilder


def retriever_node(
    state: CodePilotState,
) -> CodePilotState:
    """
    Build the repository context using RAG.
    """

    builder = ContextBuilder()

    context = builder.build(
        analysis=state["repo_analysis"],
        task=state["user_task"],
    )

    state["repository_context"] = context

    return state