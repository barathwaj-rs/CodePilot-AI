from pathlib import Path

from services.indexing.chunker import CodeChunker
from services.indexing.embedder import EmbeddingGenerator
from services.indexing.vector_store import VectorStore


class CodeIndexer:
    """
    Builds the vector database for a repository.
    """

    def __init__(self):

        self.chunker = CodeChunker()
        self.embedder = EmbeddingGenerator()
        self.store = VectorStore()

    def index_repository(
        self,
        repo_path: str,
    ):

        root = Path(repo_path)

        supported_extensions = {
            ".py",
            ".md",
        }

        documents = []
        metadatas = []
        ids = []

        chunk_id = 0

        ignore_dirs = {
        ".venv",
        ".git",
        "__pycache__",
        "storage",
        "logs",
        "chroma",
        }

        for file in root.rglob("*"):
         
            if any(part in ignore_dirs for part in file.parts):
              continue

            if (
                file.is_file()
                and file.suffix.lower() in supported_extensions
            ):

                try:

                    text = file.read_text(
                        encoding="utf-8",
                        errors="ignore",
                    )

                except Exception:
                    continue

                chunks = self.chunker.chunk(text)

                for chunk in chunks:

                    documents.append(chunk)

                    metadatas.append(
                        {
                            "file": str(file.relative_to(root)),
                        }
                    )

                    ids.append(
                        f"chunk_{chunk_id}"
                    )

                    chunk_id += 1

        embeddings = self.embedder.embed(documents)

        self.store.add(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids,
        )

       

        print(f"Indexed {len(documents)} chunks.")