from graph.state import CodePilotState


def generator(state: CodePilotState) -> CodePilotState:
    print("Generator Node")

    return state