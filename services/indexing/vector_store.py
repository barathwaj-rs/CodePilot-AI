from chromadb import PersistentClient
from config.settings import (
    CHROMA_PATH,
    COLLECTION_PREFIX,
)
from pathlib import Path
from chromadb import PersistentClient

class VectorStore:
    """
    Stores and searches embeddings.
    """

    def __init__(
        self,
        repository_name: str,
    ):

        self.client = PersistentClient(path=CHROMA_PATH)

        collection_name = (
        f"{COLLECTION_PREFIX}_"
        f"{repository_name.lower().replace('-', '_')}"
        )

        self.collection = self.client.get_or_create_collection(
        name=collection_name
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
    
    def clear(self):
        """
        Remove all vectors from the collection.
        """

        ids = self.collection.get()["ids"]

        if ids:
            self.collection.delete(ids=ids)