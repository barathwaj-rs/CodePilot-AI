from dataclasses import dataclass, field

from models.generated_file import GeneratedFile


@dataclass
class GenerationResult:
    """
    Output of the Generator Agent.
    """

    summary: str

    files: list[GeneratedFile] = field(default_factory=list)