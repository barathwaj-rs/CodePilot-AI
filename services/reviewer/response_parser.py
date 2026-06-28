import json

from models.review_result import ReviewIssue
from models.review_result import ReviewResult
from services.json_utils import JsonUtils
from services.json_repair import JsonRepair


class ReviewerResponseParser:
    """
    Parses the Reviewer Agent JSON response.
    """

    @staticmethod
    def parse(
        response: str,
    ) -> ReviewResult:

        # Extract only the JSON from the LLM response
        response = JsonRepair.repair(response)
        response = JsonUtils.extract_json(response)

        try:
            data = json.loads(response)

        except json.JSONDecodeError as e:
            raise ValueError(
                f"Invalid JSON returned by Reviewer:\n{response}"
            ) from e

        issues = [
            ReviewIssue(
                severity=issue["severity"],
                file=issue["file"],
                description=issue["description"],
            )
            for issue in data.get("issues", [])
        ]

        return ReviewResult(
            approved=data["approved"],
            summary=data["summary"],
            issues=issues,
        )