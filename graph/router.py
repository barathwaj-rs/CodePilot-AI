from graph.state import CodePilotState

MAX_RETRIES = 3


def review_router(state: CodePilotState) -> str:
    """
    Decide where to go after review.
    """

    print()
    print("=" * 60)
    print("ROUTER")
    print("=" * 60)
    print(f"Approved: {state['review_result'].approved}")
    print(f"Retries : {state['retry_count']}")

    if state["review_result"].approved:
        print("-> REPORT")
        return "report"

    if state["retry_count"] >= MAX_RETRIES:
        print("-> REPORT")
        return "report"

    print("-> RETRY")
    return "retry"