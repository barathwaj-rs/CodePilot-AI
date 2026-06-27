from langchain_ollama import OllamaEmbeddings


class EmbeddingGenerator:
    """
    Generates embeddings for code chunks.
    """

    def __init__(self):

        self.embeddings = OllamaEmbeddings(
            model="nomic-embed-text",
        )

    def embed(self, texts: list[str]):

        return self.embeddings.embed_documents(texts)