from models.repository_analysis import RepositoryAnalysis
from models.repository_context import RepositoryContext
from services.indexing.retriever import Retriever


class ContextBuilder:
    """
    Builds the complete repository context.
    """

    def build(
        self,
        analysis: RepositoryAnalysis,
        task: str,
    ) -> RepositoryContext:

        retriever = Retriever(
            analysis.git_info["repository"]
        )

        chunks = retriever.retrieve(task)

        return RepositoryContext(
            analysis=analysis,
            retrieved_chunks=chunks,
            user_task=task,
        )