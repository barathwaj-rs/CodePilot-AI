from models.execution_plan import ExecutionPlan
from models.plan_step import PlanStep

from services.generator.prompt_builder import GeneratorPromptBuilder


def main():

    plan = ExecutionPlan(
        task="Add JWT Authentication",
        summary="Implement JWT authentication.",
        relevant_files=[
            "auth.py",
            "routes.py",
        ],
        steps=[
            PlanStep(
                number=1,
                title="Create JWT Helper",
                description="Create JWT helper functions.",
            ),
            PlanStep(
                number=2,
                title="Protect Routes",
                description="Secure protected endpoints.",
            ),
        ],
        risks=[
            "Incorrect secret key",
        ],
    )

    prompt = GeneratorPromptBuilder.build(plan)

    print(prompt)


if __name__ == "__main__":
    main()