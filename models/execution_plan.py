from dataclasses import dataclass, field

from models.plan_step import PlanStep


@dataclass
class ExecutionPlan:
    """
    Represents the implementation plan produced by the Planner Agent.
    """

    task: str

    summary: str

    relevant_files: list[str] = field(default_factory=list)

    steps: list[PlanStep] = field(default_factory=list)

    risks: list[str] = field(default_factory=list)