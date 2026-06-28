from graph.state import CodePilotState
from services.planner.planner import Planner
from services.logger.workflow_logger import WorkflowLogger

def planner_node(
    state: CodePilotState,
) -> CodePilotState:
    """
    Generate an execution plan using the Planner Agent.
    """

    WorkflowLogger.log(
        state,
        "📝 Creating execution plan..."
    )

    planner = Planner()

    plan = planner.plan(
        state["repository_context"]
    )

    state["execution_plan"] = plan

    WorkflowLogger.log(
        state,
        "✅ Execution plan created."
    )

    return state