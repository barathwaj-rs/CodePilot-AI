from typing import TypedDict, Optional, List, Dict, Any


class CodePilotState(TypedDict, total=False):
    # User Input
    repo_url: str
    repo_path: str
    user_task: str

    # Repository Analysis
    repo_analysis: Dict[str, Any]

    # Code Indexing
    indexed_files: List[str]

    # RAG
    retrieved_context: List[str]

    # Planning
    plan: List[str]

    # Code Generation
    generated_code: Dict[str, str]

    # Code Review
    review_comments: List[str]

    # Testing
    test_results: Dict[str, Any]

    # Git
    git_commit_hash: str

    # Conversation History
    messages: List[Dict[str, str]]