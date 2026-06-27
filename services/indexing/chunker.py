from langchain_text_splitters import RecursiveCharacterTextSplitter


class CodeChunker:
    """
    Splits source code into overlapping chunks for embedding.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    @classmethod
    def chunk(cls, text: str) -> list[str]:
        return cls.splitter.split_text(text)