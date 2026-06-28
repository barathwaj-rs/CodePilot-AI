import json

from services.planner.response_parser import PlannerResponseParser


def main():

    fake_response = json.dumps(
        {
            "summary": "Implement JWT authentication.",

            "relevant_files": [
                "auth.py",
                "routes.py",
            ],

            "steps": [
                {
                    "number": 1,
                    "title": "Create JWT Helper",
                    "description": "Create reusable JWT utilities.",
                },
                {
                    "number": 2,
                    "title": "Update Login",
                    "description": "Return JWT after successful login.",
                },
            ],

            "risks": [
                "Existing authentication flow may break."
            ],
        }
    )

    plan = PlannerResponseParser.parse(
        task="Add JWT Authentication",
        response=fake_response,
    )

    print(plan)


if __name__ == "__main__":
    main()