from models.generated_file import GeneratedFile
from models.generation_result import GenerationResult
from services.reviewer.prompt_builder import ReviewerPromptBuilder


def main():

    result = GenerationResult(
        summary="JWT implementation",
        files=[
            GeneratedFile(
                path="auth.py",
                action="modify",
                content="""
def login():
    pass
"""
            ),
            GeneratedFile(
                path="jwt.py",
                action="create",
                content="""
def create_token():
    pass
"""
            ),
        ],
    )

    prompt = ReviewerPromptBuilder.build(
        result
    )

    print(prompt)


if __name__ == "__main__":
    main()