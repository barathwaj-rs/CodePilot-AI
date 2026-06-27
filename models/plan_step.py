from dataclasses import dataclass


@dataclass
class PlanStep:
    """
    One implementation step.
    """

    number: int
    description: str