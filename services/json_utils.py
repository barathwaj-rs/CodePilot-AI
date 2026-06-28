import re


class JsonUtils:
    """
    Utilities for extracting JSON from LLM responses.
    """

    @staticmethod
    def extract_json(response: str) -> str:
        """
        Extracts the first valid JSON object from an LLM response.
        """

        response = response.strip()

        # Remove markdown fences
        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        # Find first JSON object
        match = re.search(r"\{.*\}", response, re.DOTALL)

        if not match:
            raise ValueError(
                "No JSON object found in LLM response."
            )

        return match.group(0)