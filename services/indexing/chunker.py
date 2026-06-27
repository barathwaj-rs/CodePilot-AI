from langchain_text_splitters import RecursiveCharacterTextSplitter
from config.settings import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


class CodeChunker:
    """
    Splits source code into overlapping chunks for embedding.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    @classmethod
    def chunk(cls, text: str) -> list[str]:
        return cls.splitter.split_text(text)