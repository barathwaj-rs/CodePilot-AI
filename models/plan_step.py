from dataclasses import dataclass


@dataclass
class PlanStep:
    """
    Represents a single implementation step.
    """

    number: int

    title: str

    description: str