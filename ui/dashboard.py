import gradio as gr


def build_dashboard():

    with gr.Tabs():

        with gr.Tab("📋 Execution Plan"):

            execution = gr.Textbox(
                lines=20,
                label="Execution Plan",
            )

        with gr.Tab("💻 Generated Files"):

            generated = gr.Textbox(
                lines=20,
                label="Generated Files",
            )

        with gr.Tab("🔍 Review"):

            review = gr.Textbox(
                lines=20,
                label="Review",
            )

        with gr.Tab("🌿 Git"):

            git = gr.Textbox(
                lines=20,
                label="Git",
            )

        with gr.Tab("📄 Final Report"):

            report = gr.Textbox(
                lines=20,
                label="Final Report",
            )

        with gr.Tab("📜 Workflow"):

            workflow_logs = gr.Textbox(
                label="Workflow Logs",
                lines=20,
            )

    return (
        execution,
        generated,
        review,
        git,
        report,
        workflow_logs,
    )