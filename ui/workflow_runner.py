from graph.workflow import CodePilotWorkflow
from ui.formatters import format_workflow_logs
from services.report.report_formatter import ReportFormatter
from ui.formatters import (
    format_execution_plan,
    format_generated_files,
    format_review,
    format_git,
)

workflow = CodePilotWorkflow().build()


def run_codepilot(
    repository_path: str,
    task: str,
):
    state = workflow.invoke(
        {
            "repo_url": repository_path,
            "user_task": task,

            "retry_count": 0,

            "repo_analysis": None,
            "repository_context": None,

            "execution_plan": None,
            "generation_result": None,
            "review_result": None,

            "git_branch": None,
            "git_commit": None,
            "commit_message": None,

            "final_report": None,
            "workflow_logs": [],
        }
    )

    return (
        format_execution_plan(state),
        format_generated_files(state),
        format_review(state),
        format_git(state),
        ReportFormatter.format(state["final_report"]),
        format_workflow_logs(state),
        state,
    )