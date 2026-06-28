from langgraph.graph import END
from langgraph.graph import START
from langgraph.graph import StateGraph

from graph.state import CodePilotState

from graph.nodes.analyzer_node import analyzer_node
from graph.nodes.indexer_node import indexer_node
from graph.nodes.retriever_node import retriever_node
from graph.nodes.planner_node import planner_node
from graph.nodes.generator_node import generator_node
from graph.nodes.reviewer_node import reviewer_node
from graph.nodes.retry_node import retry_node
from graph.nodes.writer_node import writer_node
from graph.nodes.report_node import report_node

from graph.nodes.git_node import git_node
from graph.nodes.git_stage_node import git_stage_node
from graph.nodes.commit_message_node import commit_message_node
from graph.nodes.git_commit_node import git_commit_node

from graph.router import review_router


class CodePilotWorkflow:
    """
    LangGraph workflow for CodePilot AI.
    """

    def __init__(self):

        self.graph = StateGraph(
            CodePilotState,
        )

    def build(self):

        # ==========================
        # Nodes
        # ==========================

        self.graph.add_node(
            "analyzer",
            analyzer_node,
        )

        self.graph.add_node(
            "git",
            git_node,
        )

        self.graph.add_node(
            "indexer",
            indexer_node,
        )

        self.graph.add_node(
            "retriever",
            retriever_node,
        )

        self.graph.add_node(
            "planner",
            planner_node,
        )

        self.graph.add_node(
            "generator",
            generator_node,
        )

        self.graph.add_node(
            "reviewer",
            reviewer_node,
        )

        self.graph.add_node(
            "retry",
            retry_node,
        )

        self.graph.add_node(
            "writer",
            writer_node,
        )

        self.graph.add_node(
            "git_stage",
            git_stage_node,
        )

        self.graph.add_node(
            "commit_message",
            commit_message_node,
        )

        self.graph.add_node(
            "git_commit",
            git_commit_node,
        )

        self.graph.add_node(
            "report",
            report_node,
        )

        # ==========================
        # Flow
        # ==========================

        self.graph.add_edge(
            START,
            "analyzer",
        )

        self.graph.add_edge(
            "analyzer",
            "git",
        )

        self.graph.add_edge(
            "git",
            "indexer",
        )

        self.graph.add_edge(
            "indexer",
            "retriever",
        )

        self.graph.add_edge(
            "retriever",
            "planner",
        )

        self.graph.add_edge(
            "planner",
            "generator",
        )

        self.graph.add_edge(
            "generator",
            "reviewer",
        )

        self.graph.add_edge(
            "retry",
            "generator",
        )

        self.graph.add_conditional_edges(
            "reviewer",
            review_router,
            {
                "writer": "writer",
                "retry": "retry",
                "report": "report",
            },
        )

        # Success path
        self.graph.add_edge(
            "writer",
            "git_stage",
        )

        self.graph.add_edge(
            "git_stage",
            "commit_message",
        )

        self.graph.add_edge(
            "commit_message",
            "git_commit",
        )

        self.graph.add_edge(
            "git_commit",
            "report",
        )

        self.graph.add_edge(
            "report",
            END,
        )

        return self.graph.compile()