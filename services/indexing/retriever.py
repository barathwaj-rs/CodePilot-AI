from services.indexing.embedder import EmbeddingGenerator
from services.indexing.vector_store import VectorStore
from models.retrieved_chunk import RetrievedChunk
from config.settings import TOP_K_RESULTS

class Retriever:
    """
    Retrieves relevant code chunks.
    """

    def __init__(
    self,
    repository_name: str,
    ):

        self.embedder = EmbeddingGenerator()

        self.store = VectorStore(
        repository_name
        )

    def retrieve(
    self,
    query: str,
    n_results: int = TOP_K_RESULTS,
    ) -> list[RetrievedChunk]:

        embedding = self.embedder.embed([query])[0]

        results = self.store.search(
        embedding,
        n_results=n_results,
        )

        retrieved = []

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        for document, metadata, distance in zip(
        documents,
        metadatas,
        distances,
        ):

          retrieved.append(
            RetrievedChunk(
                file=metadata["file"],
                content=document,
                score=distance,
            )
          )

        return retrieved