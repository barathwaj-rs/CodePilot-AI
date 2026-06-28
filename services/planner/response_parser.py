import json

from models.execution_plan import ExecutionPlan
from models.plan_step import PlanStep
from services.json_utils import JsonUtils
from services.json_repair import JsonRepair


class PlannerResponseParser:

    @staticmethod
    def parse(
        task: str,
        response: str,
    ) -> ExecutionPlan:

        response = JsonRepair.repair(response)

        response = JsonUtils.extract_json(response)

        try:
            data = json.loads(response)

        except json.JSONDecodeError as e:
            raise ValueError(
                f"Invalid JSON returned by Planner:\n{response}"
            ) from e

        steps = [
            PlanStep(
                number=step["number"],
                title=step["title"],
                description=step["description"],
            )
            for step in data.get("steps", [])
        ]

        return ExecutionPlan(
            task=task,
            summary=data.get("summary", ""),
            relevant_files=data.get("relevant_files", []),
            steps=steps,
            risks=data.get("risks", []),
        )