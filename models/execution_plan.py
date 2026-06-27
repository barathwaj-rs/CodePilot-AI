from dataclasses import dataclass, field


@dataclass
class ExecutionPlan:
    """
    High-level plan produced by the Planner.
    """

    steps: list[str] = field(default_factory=list)

    reasoning: str = ""