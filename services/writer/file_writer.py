from pathlib import Path

from models.generation_result import GenerationResult


class FileWriter:
    """
    Writes generated files into the repository.
    """

    @staticmethod
    def write(
        repository_path: str,
        generation: GenerationResult,
    ) -> None:

        repository = Path(repository_path)

        for file in generation.files:

            path = repository / file.path

            path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            path.write_text(
                file.content,
                encoding="utf-8",
            )