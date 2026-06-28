from models.generation_result import GenerationResult
from models.repository_analysis import RepositoryAnalysis
from models.retrieved_chunk import RetrievedChunk

from services.indexing.indexer import CodeIndexer
from services.rag.retriever import Retriever
from services.repository.analyzer import RepositoryAnalyzer
from services.writer.file_writer import FileWriter


class RepositoryService:
    """
    High-level interface for repository operations.
    """

    def __init__(
        self,
        repository_name: str,
    ):

        self.repository_name = repository_name

        self.indexer = CodeIndexer(
            repository_name,
        )

        self.retriever = Retriever(
            repository_name,
        )

    def analyze(
        self,
        repository_path: str,
    ) -> RepositoryAnalysis:

        return RepositoryAnalyzer.analyze(
            repository_path,
        )

    def index(
        self,
        repository_path: str,
    ) -> None:

        self.indexer.index(
            repository_path,
        )

    def retrieve(
        self,
        query: str,
    ) -> list[RetrievedChunk]:

        return self.retriever.retrieve(
            query,
        )

    def write(
        self,
        repository_path: str,
        generation: GenerationResult,
    ) -> None:

        FileWriter.write(
            repository_path,
            generation,
        )