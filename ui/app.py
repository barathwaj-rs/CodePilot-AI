import gradio as gr

from graph.workflow import CodePilotWorkflow
from services.report.report_formatter import ReportFormatter
from services.apply_changes.apply_service import ApplyChangesService


# ==========================================
# Build Workflow
# ==========================================

workflow = CodePilotWorkflow().build()


# ==========================================
# Generate Workflow
# ==========================================

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
        }
    )

    print("=" * 60)
    print("Workflow finished.")
    print("=" * 60)

    report = ReportFormatter.format(
        state["final_report"]
    )

    print("Report formatted.")

    return (
        report,
        state,
    )


# ==========================================
# Apply Changes
# ==========================================

def apply_changes(
    state,
):

    if state is None:
        return (
            "No generated workflow found.\n"
            "Please click Generate first."
        )

    if not state["review_result"].approved:
        return (
            "❌ Changes cannot be applied.\n\n"
            "The generated code was not approved by the reviewer."
        )

    try:

        ApplyChangesService.apply(state)

    except Exception as e:

        return f"❌ {str(e)}"

    output = []

    output.append("✅ Changes applied successfully.")
    output.append("")

    if state.get("git_branch"):
        output.append(
            f"Branch : {state['git_branch']}"
        )

    if state.get("git_commit"):
        output.append(
            f"Commit : {state['git_commit']}"
        )

    if state.get("commit_message"):
        output.append(
            f"Message: {state['commit_message']}"
        )

    return "\n".join(output)


# ==========================================
# UI
# ==========================================

with gr.Blocks(
    title="CodePilot AI",
) as demo:

    # Per-user workflow state
    workflow_state = gr.State()

    gr.Markdown("# 🤖 CodePilot AI")

    gr.Markdown(
        "### AI Software Engineering Agent"
    )

    repository = gr.Textbox(
        label="Repository Path",
        placeholder="C:\\Projects\\MyApp",
    )

    task = gr.Textbox(
        label="Task",
        lines=4,
        placeholder="Add JWT Authentication",
    )

    generate_button = gr.Button(
        "🚀 Generate"
    )

    report = gr.Textbox(
        label="Final Report",
        lines=25,
    )

    apply_button = gr.Button(
        "✅ Apply Changes"
    )

    apply_result = gr.Textbox(
        label="Apply Result",
        lines=6,
    )

    # Generate workflow
    generate_button.click(
        fn=run_codepilot,
        inputs=[
            repository,
            task,
        ],
        outputs=[
            report,
            workflow_state,
        ],
    )

    # Apply approved changes
    apply_button.click(
        fn=apply_changes,
        inputs=workflow_state,
        outputs=apply_result,
    )


demo.launch()