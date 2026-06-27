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

    readme = (
    analysis.readme_summary
    if analysis.readme_summary
    else "-"
    )

    git_info = (
    f"Repository : {analysis.git_info.get('repository', '-')}\n"
    f"Branch     : {analysis.git_info.get('branch', '-')}\n"
    f"Author     : {analysis.git_info.get('author', '-')}\n"
    f"Commit     : {analysis.git_info.get('last_commit', '-')}\n"
    f"Message    : {analysis.git_info.get('last_message', '-')}\n"
    f"Remote     : {analysis.git_info.get('remote', '-') or '-'}"
    )

    statistics = "\n".join(
    f"{k}: {v}"
    for k, v in analysis.statistics.items()
    )

    return (
        len(analysis.files),
        languages,
        frameworks,
        dependencies,
        entry_points,
        readme,
        git_info,
        statistics,
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

    with gr.Row():

        readme_box = gr.Textbox(
            label="README",
            lines=15
        )   

    with gr.Row():

        git_box = gr.Textbox(
            label="Git Information",
            lines=8
        )

        statistics = gr.Textbox(
            label="Repository Statistics",
            lines=8,
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
            readme_box,
            git_box,
            statistics
        ],
    )

demo.launch()