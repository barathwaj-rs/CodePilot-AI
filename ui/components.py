import gradio as gr

from ui.dashboard import build_dashboard


def build_components():

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

    (
        execution_plan,
        generated_files,
        review,
        git,
        report,
        workflow_logs,
    ) = build_dashboard()

    apply_button = gr.Button(
        "✅ Apply Changes"
    )

    apply_result = gr.Textbox(
        label="Apply Result",
        lines=6,
    )

    return (
        repository,
        task,
        generate_button,
        execution_plan,
        generated_files,
        review,
        git,
        report,
        workflow_logs,
        workflow_state,
        apply_button,
        apply_result,
    )