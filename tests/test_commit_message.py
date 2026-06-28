from services.commit_message.commit_message_generator import (
    CommitMessageGenerator,
)

from models.generation_result import (
    GenerationResult,
    GeneratedFile,
)

from models.review_result import (
    ReviewResult,
    ReviewIssue,
)


def main():

    generator = CommitMessageGenerator()

    message = generator.generate(

        GenerationResult(

            summary="Added JWT authentication",

            files=[

                GeneratedFile(
                    path="auth.py",
                    action="modify",
                    content=""
                ),

                GeneratedFile(
                    path="routes.py",
                    action="modify",
                    content=""
                ),

            ],

        ),

        ReviewResult(

            approved=True,

            summary="Looks good",

            issues=[
                ReviewIssue(
                    severity="LOW",
                    file="auth.py",
                    description="Secret key should come from environment."
                )
            ],

        ),

    )

    print(message)


if __name__ == "__main__":
    main()