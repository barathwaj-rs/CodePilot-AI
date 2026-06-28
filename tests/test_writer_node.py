from graph.nodes.analyzer_node import analyzer_node
from graph.nodes.indexer_node import indexer_node
from graph.nodes.retriever_node import retriever_node
from graph.nodes.planner_node import planner_node
from graph.nodes.generator_node import generator_node
from graph.nodes.writer_node import writer_node


def main():

    state = {
        "repo_url": "storage/test_repo",
        "user_task": "Add JWT Authentication",

        "repo_analysis": None,
        "repository_context": None,
        "execution_plan": None,
        "generation_result": None,
        "review_report": None,
        "final_response": None,
    }

    state = analyzer_node(state)
    state = indexer_node(state)
    state = retriever_node(state)
    state = planner_node(state)
    state = generator_node(state)
    state = writer_node(state)

    print("Files written successfully!")


if __name__ == "__main__":
    main()