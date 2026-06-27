from dataclasses import dataclass, field

from models.repository_analysis import RepositoryAnalysis
from models.retrieved_chunk import RetrievedChunk


@dataclass
class RepositoryContext:
    """
    Everything the AI needs about a repository.
    """

    analysis: RepositoryAnalysis

    retrieved_chunks: list[RetrievedChunk] = field(default_factory=list)

    user_task: str = ""