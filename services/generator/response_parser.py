import json

from models.generated_file import GeneratedFile
from models.generation_result import GenerationResult
from services.json_utils import JsonUtils
from services.json_repair import JsonRepair

class GeneratorResponseParser:
    """
    Converts the Generator LLM response into a GenerationResult.
    """

    @staticmethod
    def parse(
        response: str,
    ) -> GenerationResult:

        # Remove whitespace
        response = JsonRepair.repair(response)
        response = JsonUtils.extract_json(response)

        # Parse JSON
        try:
            data = json.loads(response)

        except json.JSONDecodeError as e:
            raise ValueError(
                "Generator returned invalid JSON.\n\n"
                f"{response}"
            ) from e

        # Validate JSON structure
        if "files" not in data:
            raise ValueError(
                "Generator JSON does not contain a 'files' field."
            )

        files = []

        for file in data["files"]:

            try:

                files.append(
                    GeneratedFile(
                        path=file["path"],
                        action=file["action"],
                        content=file["content"],
                    )
                )

            except KeyError as e:

                raise ValueError(
                    f"Missing field in generated file: {e}"
                ) from e

        return GenerationResult(
            summary=data.get("summary", ""),
            files=files,
        )