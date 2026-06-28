from graph.state import CodePilotState
from services.reviewer.reviewer import Reviewer


def reviewer_node(
    state: CodePilotState,
) -> CodePilotState:
    """
    Review the generated code.
    """

    reviewer = Reviewer()

    result = reviewer.review(
        state["generation_result"]
    )

    state["review_result"] = result

    return state