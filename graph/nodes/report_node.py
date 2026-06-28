from graph.state import CodePilotState
from services.report.final_report_builder import FinalReportBuilder
from services.logger.workflow_logger import WorkflowLogger

def report_node(state: CodePilotState) -> CodePilotState:

    print()
    print("=" * 60)
    print("REPORT NODE")
    print("=" * 60)

    state["final_report"] = FinalReportBuilder.build(state)

    print("Report built successfully.")

    WorkflowLogger.log(
        state,
        "📄 Final report generated."
    )

    return state