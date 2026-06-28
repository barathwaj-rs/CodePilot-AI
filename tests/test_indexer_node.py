from graph.nodes.indexer_node import indexer_node


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

    state = indexer_node(state)

    print("Repository indexed successfully!")


if __name__ == "__main__":
    main()