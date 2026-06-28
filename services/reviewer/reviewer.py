from services.llm_service import LLMService

from models.generation_result import GenerationResult
from services.reviewer.prompt_builder import ReviewerPromptBuilder
from services.reviewer.response_parser import ReviewerResponseParser


class Reviewer:
    """
    AI Reviewer Agent.
    """

    

    def review(
        self,
        generation: GenerationResult,
    ):

        prompt = ReviewerPromptBuilder.build(
            generation,
        )

        print("\n" + "=" * 60)
        print("REVIEWER")
        print("=" * 60)

        print("Reviewer prompt built.")
        print(f"Reviewer prompt length: {len(prompt):,} characters")

        print("Calling LLM...")

        result = LLMService.invoke_json(
            prompt,
            ReviewerResponseParser,
        )

        print("\nFirst 500 characters of reviewer prompt:\n")
        print(prompt[:500])

        print("\nReviewer prompt length:", len(prompt))

        print("Reviewer completed.")

        return result