from models.generation_result import GenerationResult
from models.review_result import ReviewResult


class CommitMessagePromptBuilder:
    """
    Builds prompts for AI-generated Git commit messages.
    """

    @staticmethod
    def build(
        generation: GenerationResult,
        review: ReviewResult,
    ) -> str:

        files = "\n".join(
            file.path
            for file in generation.files
        )

        issues = "\n".join(
            f"- {issue.description}"
            for issue in review.issues
        )

        return f"""
You are an experienced software engineer.

Generate a professional Git commit message.

Use Conventional Commit format.

Examples

feat(auth): implement JWT authentication

fix(api): resolve login validation bug

refactor(core): simplify repository indexing

==========================
Implementation Summary
==========================

{generation.summary}

==========================
Files Changed
==========================

{files}

==========================
Reviewer Notes
==========================

{issues}

Rules

- Return ONLY the commit message.
- One line only.
- No markdown.
- No quotes.
"""