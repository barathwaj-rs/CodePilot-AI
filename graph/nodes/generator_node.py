from graph.state import CodePilotState
from services.generator.generator import Generator
from services.logger.workflow_logger import WorkflowLogger

def generator_node(
    state: CodePilotState,
) -> CodePilotState:
    """
    Generate code modifications from the execution plan.
    """

    WorkflowLogger.log(
        state,
        "⚙️ Generating code..."
    )

    generator = Generator()

    result = generator.generate(
    plan=state["execution_plan"],
    previous_review=state["review_result"],
    )

    state["generation_result"] = result

    WorkflowLogger.log(
        state,
        "✅ Code generation completed."
    )

    return state