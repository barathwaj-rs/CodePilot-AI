import json

from services.generator.response_parser import GeneratorResponseParser


def main():

    fake_response = json.dumps(
        {
            "summary": "Implemented JWT authentication.",

            "files": [
                {
                    "path": "auth.py",
                    "action": "modify",
                    "content": "def login():\n    pass",
                },
                {
                    "path": "utils/jwt.py",
                    "action": "create",
                    "content": "def create_token():\n    pass",
                },
            ],
        }
    )

    result = GeneratorResponseParser.parse(
        fake_response,
    )

    print(result)


if __name__ == "__main__":
    main()