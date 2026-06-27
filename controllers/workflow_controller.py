from graph.workflow import workflow


class WorkflowController:

    @staticmethod
    def run(repo_url: str, user_task: str):

        initial_state = {
            "repo_url": repo_url,
            "user_task": user_task,
        }

        final_state = workflow.invoke(initial_state)

        return final_state