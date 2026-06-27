from services.indexing.embedder import EmbeddingGenerator
from services.indexing.vector_store import VectorStore
from models.retrieved_chunk import RetrievedChunk


class Retriever:
    """
    Retrieves relevant code chunks.
    """

    def __init__(self):

        self.embedder = EmbeddingGenerator()
        self.store = VectorStore()

    def retrieve(
    self,
    query: str,
    n_results: int = 5,
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