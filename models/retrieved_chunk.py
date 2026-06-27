from dataclasses import dataclass


@dataclass
class RetrievedChunk:
    """
    Represents one retrieved code chunk.
    """

    file: str

    content: str

    score: float