from models.execution_plan import ExecutionPlan
from models.plan_step import PlanStep

from services.generator.generator import Generator


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

    generator = Generator()

    result = generator.generate(plan)

    print(result)


if __name__ == "__main__":
    main()