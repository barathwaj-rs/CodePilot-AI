from graph.state import CodePilotState
from services.generator.generator import Generator


def generator_node(
    state: CodePilotState,
) -> CodePilotState:
    """
    Generate code modifications from the execution plan.
    """

    generator = Generator()

    result = generator.generate(
    plan=state["execution_plan"],
    previous_review=state["review_result"],
    )

    state["generation_result"] = result

    return state