from graph.state import CodePilotState
from services.writer.file_writer import FileWriter


def writer_node(
    state: CodePilotState,
) -> CodePilotState:
    """
    Writes approved generated files into the repository.
    """

    FileWriter.write(
        repository_path=state["repo_url"],
        generation=state["generation_result"],
    )

    return state