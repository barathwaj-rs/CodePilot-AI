import gradio as gr

from controllers.workflow_controller import WorkflowController

def run_workflow():

    result = WorkflowController.run(
        repo_url="https://github.com/example/project",
        user_task="Add JWT Authentication",
    )

    analysis = result["repo_analysis"]

    output = []

    output.append("Repository Analysis")
    output.append("")
    output.append(f"Files: {len(analysis.files)}")
    output.append("")

    output.append("Languages:")

    for language, count in analysis.languages.items():
        output.append(f"- {language}: {count}")

    return "\n".join(output)


import gradio as gr

from controllers.workflow_controller import WorkflowController


def run_workflow(repo_url, task):

    result = WorkflowController.run(
        repo_url=repo_url,
        user_task=task
    )

    analysis = result["repo_analysis"]

    languages = "\n".join(
        f"{lang}: {count}"
        for lang, count in analysis.languages.items()
    )

    frameworks = "\n".join(analysis.frameworks) if analysis.frameworks else "-"

    dependencies = (
        "\n".join(
            f"{k}: {', '.join(v)}"
            for k, v in analysis.dependencies.items()
        )
        if analysis.dependencies
        else "-"
    )

    entry_points = (
        "\n".join(analysis.entry_points)
        if analysis.entry_points
        else "-"
    )

    return (
        len(analysis.files),
        languages,
        frameworks,
        dependencies,
        entry_points,
    )


with gr.Blocks(title="CodePilot AI") as demo:

    gr.Markdown("# 🚀 CodePilot AI")
    gr.Markdown("### AI Software Engineering Agent")

    repo_url = gr.Textbox(
        label="Repository URL",
        placeholder="https://github.com/user/repository"
    )

    task = gr.Textbox(
        label="Task",
        placeholder="What would you like CodePilot AI to do?"
    )

    analyze_btn = gr.Button("Analyze Repository")

    with gr.Row():

        file_count = gr.Number(label="Files")

        languages = gr.Textbox(
            label="Languages",
            lines=8
        )

        frameworks = gr.Textbox(
            label="Frameworks",
            lines=8
        )

    with gr.Row():

        dependencies = gr.Textbox(
            label="Dependencies",
            lines=8
        )

        entry_points = gr.Textbox(
            label="Entry Points",
            lines=8
        )

    analyze_btn.click(
        fn=run_workflow,
        inputs=[
            repo_url,
            task
        ],
        outputs=[
            file_count,
            languages,
            frameworks,
            dependencies,
            entry_points,
        ],
    )

demo.launch()