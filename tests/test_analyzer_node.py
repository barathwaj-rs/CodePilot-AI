from graph.nodes.analyzer_node import analyzer_node


def main():

    state = {
        "repo_url": ".",
        "user_task": "Add JWT Authentication",

        "repo_analysis": None,
        "repository_context": None,
        "execution_plan": None,
        "generation_result": None,
        "review_report": None,
        "final_response": None,
    }

    state = analyzer_node(state)

    print(state["repo_analysis"])


if __name__ == "__main__":
    main()