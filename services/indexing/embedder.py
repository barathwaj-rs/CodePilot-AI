from langchain_ollama import OllamaEmbeddings
from config.settings import EMBEDDING_MODEL

class EmbeddingGenerator:
    """
    Generates embeddings for code chunks.
    """

    def __init__(self):

        self.embeddings = OllamaEmbeddings(
            model=EMBEDDING_MODEL,
        )

    def embed(self, texts: list[str]):

        return self.embeddings.embed_documents(texts)