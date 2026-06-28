from graph.state import CodePilotState
from services.rag.context_builder import ContextBuilder
from services.logger.workflow_logger import WorkflowLogger

def retriever_node(
    state: CodePilotState,
) -> CodePilotState:
    """
    Build the repository context using RAG.
    """

    WorkflowLogger.log(
        state,
        "🔎 Retrieving relevant files..."
    )

    builder = ContextBuilder()

    context = builder.build(
        analysis=state["repo_analysis"],
        task=state["user_task"],
    )

    state["repository_context"] = context

    WorkflowLogger.log(
        state,
        "✅ Retrieval completed."
    )

    return state