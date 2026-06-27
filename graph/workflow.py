from langgraph.graph import StateGraph, START, END

from graph.state import CodePilotState

from graph.nodes.clone_repo import clone_repo
from graph.nodes.repository_analyzer import repository_analyzer
from graph.nodes.code_indexer import code_indexer
from graph.nodes.planner import planner
from graph.nodes.generator import generator
from graph.nodes.reviewer import reviewer
from graph.nodes.test_runner import test_runner


# Create the graph
builder = StateGraph(CodePilotState)

# Add nodes
builder.add_node("clone_repo", clone_repo)
builder.add_node("repository_analyzer", repository_analyzer)
builder.add_node("code_indexer", code_indexer)
builder.add_node("planner", planner)
builder.add_node("generator", generator)
builder.add_node("reviewer", reviewer)
builder.add_node("test_runner", test_runner)

# Connect nodes
builder.add_edge(START, "clone_repo")
builder.add_edge("clone_repo", "repository_analyzer")
builder.add_edge("repository_analyzer", "code_indexer")
builder.add_edge("code_indexer", "planner")
builder.add_edge("planner", "generator")
builder.add_edge("generator", "reviewer")
builder.add_edge("reviewer", "test_runner")
builder.add_edge("test_runner", END)

# Compile graph
workflow = builder.compile()