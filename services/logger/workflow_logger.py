class WorkflowLogger:
    """
    Stores workflow progress messages.
    """

    @staticmethod
    def log(
        state,
        message: str,
    ):

        state["workflow_logs"].append(message)

        print(message)