from models.generation_result import GenerationResult


class ReviewerPromptBuilder:
    """
    Builds prompts for the Reviewer Agent.
    """

    @staticmethod
    def build(
        generation: GenerationResult,
    ) -> str:

        files = ""

        for file in generation.files:

            files += f"""
==================================================
File
==================================================

Path:
{file.path}

Action:
{file.action}

Content:

{file.content}

"""

        prompt = f"""
You are an expert Senior Software Engineer performing a code review.

Your responsibility is to review AI-generated code before it is written to the repository.

IMPORTANT RULES

- Carefully inspect every generated file.
- Look for bugs.
- Look for syntax errors.
- Look for missing imports.
- Look for undefined variables.
- Look for incorrect function calls.
- Look for security issues.
- Look for bad coding practices.
- Return ONLY valid JSON.
- Do NOT explain your reasoning.
- Do NOT include markdown.
- If any HIGH severity issue exists, approved MUST be false.
- If any MEDIUM severity issue exists, approved MUST be false.
- approved=true only if the generated code is production-ready.
- If there are only LOW severity issues, approved may be true.

==================================================
Generated Files
==================================================

{files}

==================================================
Required JSON Format
==================================================

{{
    "approved": true,

    "summary": "...",

    "issues": [
        {{
            "severity": "low",
            "file": "auth.py",
            "description": "..."
        }}
    ]
}}

Return ONLY valid JSON.
"""
        print(f"Reviewer prompt size: {len(prompt):,} characters")
        return prompt