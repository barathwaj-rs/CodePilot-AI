from services.llm_service import LLMService
from services.planner.prompt_builder import PlannerPromptBuilder
from services.planner.response_parser import PlannerResponseParser

from models.execution_plan import ExecutionPlan
from models.repository_context import RepositoryContext


class Planner:
    """
    AI Planner Agent.
    """

    def plan(
        self,
        context: RepositoryContext,
    ) -> ExecutionPlan:

        prompt = PlannerPromptBuilder.build(
            context,
        )

        return LLMService.invoke_json(
            prompt,
            PlannerResponseParser,
            context.user_task,
        )