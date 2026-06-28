from pathlib import Path

from models.generated_file import GeneratedFile
from models.generation_result import GenerationResult

from services.writer.file_writer import FileWriter


def main():

    repository = "storage/test_repo"

    generation = GenerationResult(

        summary="Demo",

        files=[

            GeneratedFile(
                path="hello.py",
                action="create",
                content='print("Hello CodePilot")',
            ),

            GeneratedFile(
                path="folder/test.py",
                action="create",
                content="x = 10",
            ),

        ],
    )

    FileWriter.write(
        repository,
        generation,
    )

    print("Files written!")

    print(Path(repository).resolve())


if __name__ == "__main__":
    main()