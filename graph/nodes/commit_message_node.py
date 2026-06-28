from graph.state import CodePilotState

from services.commit_message.commit_message_generator import (
    CommitMessageGenerator,
)


def commit_message_node(
    state: CodePilotState,
) -> CodePilotState:
    """
    Generate an AI commit message.
    """

    generator = CommitMessageGenerator()

    message = generator.generate(
        state["generation_result"],
        state["review_result"],
    )

    state["commit_message"] = message

    print()
    print("=" * 60)
    print("COMMIT MESSAGE")
    print("=" * 60)
    print(message)

    return state