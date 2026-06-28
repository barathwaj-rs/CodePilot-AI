from services.llm_service import LLMService

from models.execution_plan import ExecutionPlan
from models.generation_result import GenerationResult
from models.review_result import ReviewResult

from services.generator.prompt_builder import GeneratorPromptBuilder
from services.generator.response_parser import GeneratorResponseParser


class Generator:
    """
    AI Generator Agent.
    """

    def generate(
        self,
        plan: ExecutionPlan,
        previous_review: ReviewResult | None = None,
    ) -> GenerationResult:

        prompt = GeneratorPromptBuilder.build(
            plan=plan,
            previous_review=previous_review,
        )

        return LLMService.invoke_json(
            prompt=prompt,
            parser=GeneratorResponseParser,
        )