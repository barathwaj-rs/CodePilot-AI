from typing import Type

from ollama import Client

from config import settings


class LLMService:
    """
    Centralized LLM service using the official Ollama client.
    """

    _client = None

    @classmethod
    def get_client(cls) -> Client:

        if cls._client is None:

            cls._client = Client(
                host=settings.OLLAMA_BASE_URL,
            )

        return cls._client

    @classmethod
    def invoke_json(
        cls,
        prompt: str,
        parser: Type,
        *parser_args,
        max_retries: int = 3,
    ):

        client = cls.get_client()

        last_error = None

        for attempt in range(max_retries):

            print("\n" + "=" * 60)
            print(f"LLM Attempt {attempt + 1}/{max_retries}")
            print("=" * 60)

            print("Sending prompt to Ollama...")

            response = client.chat(
                model=settings.OLLAMA_MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )

            print("Response received from Ollama.")

            content = response["message"]["content"]

            try:

                print("Parsing JSON response...")

                result = parser.parse(
                    *parser_args,
                    content,
                )

                print("JSON parsed successfully.")

                return result

            except ValueError as error:

                print("JSON parsing failed.")
                print(error)

                last_error = error

        raise last_error