from dataclasses import dataclass, field

from models.plan_step import PlanStep


@dataclass
class ExecutionPlan:
    """
    Complete implementation plan.
    """

    task: str

    relevant_files: list[str] = field(default_factory=list)

    steps: list[PlanStep] = field(default_factory=list)