from services.report.report_formatter import ReportFormatter


def format_execution_plan(state):

    plan = state["execution_plan"]

    if plan is None:
        return "No execution plan."

    output = []

    output.append(f"Task: {plan.task}")
    output.append("")
    output.append(f"Summary: {plan.summary}")
    output.append("")
    output.append("Relevant Files")

    for file in plan.relevant_files:
        output.append(f"• {file}")

    output.append("")
    output.append("Steps")

    for step in plan.steps:
        output.append(
            f"{step.number}. {step.title}"
        )

    output.append("")
    output.append("Risks")

    for risk in plan.risks:
        output.append(f"• {risk}")

    return "\n".join(output)


def format_generated_files(state):

    generation = state["generation_result"]

    if generation is None:
        return "No generated files."

    output = []

    for file in generation.files:

        output.append("=" * 60)
        output.append(file.path)
        output.append("=" * 60)
        output.append(file.content)
        output.append("")

    return "\n".join(output)


def format_review(state):

    review = state["review_result"]

    if review is None:
        return "No review."

    output = []

    output.append(
        f"Approved : {review.approved}"
    )

    output.append("")

    output.append(
        f"Summary : {review.summary}"
    )

    output.append("")

    output.append("Issues")

    for issue in review.issues:

        output.append(
            f"[{issue.severity.upper()}] "
            f"{issue.file}"
        )

        output.append(issue.description)

        output.append("")

    return "\n".join(output)


def format_git(state):

    output = []

    output.append(
        f"Branch : {state.get('git_branch', '')}"
    )

    output.append("")

    output.append(
        f"Commit : {state.get('git_commit', '')}"
    )

    output.append("")

    output.append(
        f"Message : {state.get('commit_message', '')}"
    )

    return "\n".join(output)


def format_workflow_logs(
    state,
):

    logs = state.get(
        "workflow_logs",
        [],
    )

    if not logs:
        return "No logs."

    return "\n".join(logs)