from services.reviewer.response_parser import ReviewerResponseParser


def main():

    response = """
{
    "approved": false,
    "summary": "Several issues were found.",

    "issues": [
        {
            "severity": "high",
            "file": "auth.py",
            "description": "Undefined variable 'SECRET'."
        },
        {
            "severity": "medium",
            "file": "routes.py",
            "description": "Missing import for request."
        }
    ]
}
"""

    result = ReviewerResponseParser.parse(
        response
    )

    print(result)


if __name__ == "__main__":
    main()