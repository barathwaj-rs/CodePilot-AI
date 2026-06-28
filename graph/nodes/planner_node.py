from graph.state import CodePilotState
from services.planner.planner import Planner


def planner_node(
    state: CodePilotState,
) -> CodePilotState:
    """
    Generate an execution plan using the Planner Agent.
    """

    planner = Planner()

    plan = planner.plan(
        state["repository_context"]
    )

    state["execution_plan"] = plan

    return state