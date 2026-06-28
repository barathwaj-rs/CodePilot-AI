from models.generated_file import GeneratedFile
from models.generation_result import GenerationResult

from services.reviewer.reviewer import Reviewer


def main():

    generation = GenerationResult(
        summary="JWT implementation",
        files=[
            GeneratedFile(
                path="auth.py",
                action="modify",
                content="""
SECRET = "abc"

def login():
    return create_token(user)
""",
            ),
        ],
    )

    reviewer = Reviewer()

    result = reviewer.review(
        generation,
    )

    print(result)


if __name__ == "__main__":
    main()