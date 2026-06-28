from ollama import Client

from config import settings

from models.generation_result import GenerationResult
from models.review_result import ReviewResult

from services.commit_message.prompt_builder import (
    CommitMessagePromptBuilder,
)


class CommitMessageGenerator:
    """
    Generates professional Git commit messages.
    """

    VALID_PREFIXES = (
        "feat",
        "fix",
        "docs",
        "style",
        "refactor",
        "perf",
        "test",
        "build",
        "ci",
        "chore",
    )

    def __init__(self):

        self.client = Client(
            host=settings.OLLAMA_BASE_URL,
        )

    def generate(
        self,
        generation: GenerationResult,
        review: ReviewResult,
    ) -> str:

        prompt = CommitMessagePromptBuilder.build(
            generation,
            review,
        )

        response = self.client.chat(
            model=settings.OLLAMA_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        message = response["message"]["content"].strip()

        # Remove markdown code fences
        message = message.replace("```", "").strip()

        # Return the first valid Conventional Commit line
        for line in message.splitlines():

            line = line.strip()

            if any(
                line.startswith(prefix)
                for prefix in self.VALID_PREFIXES
            ):
                return line

        # Fallback if the model ignored instructions
        return "chore: update project files"