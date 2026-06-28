from graph.state import CodePilotState

from graph.nodes.writer_node import writer_node
from graph.nodes.git_stage_node import git_stage_node
from graph.nodes.commit_message_node import commit_message_node
from graph.nodes.git_commit_node import git_commit_node


class ApplyChangesService:
    """
    Applies approved code changes to the repository.
    """

    @staticmethod
    def apply(
        state: CodePilotState,
    ) -> CodePilotState:

        if not state["review_result"].approved:
            raise RuntimeError(
                "Cannot apply changes because the review was not approved."
            )

        writer_node(state)

        git_stage_node(state)

        commit_message_node(state)

        git_commit_node(state)

        return state