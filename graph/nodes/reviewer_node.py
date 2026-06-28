from graph.state import CodePilotState
from services.reviewer.reviewer import Reviewer
from services.logger.workflow_logger import WorkflowLogger

def reviewer_node(
    state: CodePilotState,
) -> CodePilotState:
    """
    Review the generated code.
    """

    WorkflowLogger.log(
        state,
        "🔍 Reviewing generated code..."
    )

    reviewer = Reviewer()

    result = reviewer.review(
    state["generation_result"]
    )

    state["review_result"] = result

    if result.approved:

        WorkflowLogger.log(
            state,
            "✅ Review approved. Proceeding to final report."
        )

    else:

        WorkflowLogger.log(
            state,
            f"❌ Review failed ({len(result.issues)} issue(s) found)."
        )

    return state

    