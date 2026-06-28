from graph.state import CodePilotState

MAX_RETRIES = 3


def review_router(state: CodePilotState):

    if state["review_result"].approved:
        return "writer"

    if state["retry_count"] >= MAX_RETRIES:
        return "report"

    return "retry"