import re


class JsonRepair:
    """
    Repairs common JSON mistakes made by LLMs.
    """

    @staticmethod
    def repair(response: str) -> str:

        # Remove markdown fences
        response = response.replace("```json", "")
        response = response.replace("```", "")

        # Remove leading/trailing whitespace
        response = response.strip()

        # --------------------------------------------------
        # Fix triple quoted content strings
        # --------------------------------------------------

        pattern = r'"content"\s*:\s*"""(.*?)"""'

        def replace(match):

            code = match.group(1)

            code = (
                code
                .replace("\\", "\\\\")
                .replace('"', '\\"')
                .replace("\r", "")
                .replace("\n", "\\n")
            )

            return f'"content": "{code}"'

        response = re.sub(
            pattern,
            replace,
            response,
            flags=re.DOTALL,
        )

        return response