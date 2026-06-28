from graph.state import CodePilotState
from services.report.final_report_builder import FinalReportBuilder


def report_node(
    state: CodePilotState,
) -> CodePilotState:
    """
    Builds the final report.
    """

    state["final_report"] = FinalReportBuilder.build(state)

    return state