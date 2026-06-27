from chromadb import PersistentClient


class VectorStore:
    """
    Stores and searches embeddings.
    """

    def __init__(self):

        self.client = PersistentClient(path="./storage/chroma")

        self.collection = self.client.get_or_create_collection(
            name="codepilot"
        )

    def add(
        self,
        documents: list[str],
        embeddings: list[list[float]],
        metadatas: list[dict],
        ids: list[str],
    ):

        self.collection.add(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids,
        )

    def search(
    self,
    query_embedding: list[float],
    n_results: int = 5,
    ):

        return self.collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        )