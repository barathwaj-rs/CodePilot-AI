import gradio as gr

from ui.components import build_components
from ui.workflow_runner import run_codepilot
from ui.apply_runner import apply_changes


with gr.Blocks(
    title="CodePilot AI",
) as demo:

    (
        repository,
        task,
        generate_button,
        execution_plan,
        generated_files,
        review,
        git,
        report,
        workflow_state,
        apply_button,
        apply_result,
    ) = build_components()

    generate_button.click(
        fn=run_codepilot,
        inputs=[
            repository,
            task,
        ],
        outputs=[
            execution_plan,
            generated_files,
            review,
            git,
            report,
            workflow_state,
        ],
    )

    apply_button.click(
        fn=apply_changes,
        inputs=workflow_state,
        outputs=apply_result,
    )


if __name__ == "__main__":
    demo.launch()