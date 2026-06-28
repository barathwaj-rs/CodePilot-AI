from graph.state import CodePilotState


def retry_node(
    state: CodePilotState,
) -> CodePilotState:
    """
    Increments the retry counter before
    regenerating code.
    """

    state["retry_count"] += 1

    print()
    print("=" * 60)
    print(f"Retry Attempt {state['retry_count']}")
    print("=" * 60)

    return state