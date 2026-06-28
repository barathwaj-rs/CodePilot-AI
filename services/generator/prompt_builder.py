from models.execution_plan import ExecutionPlan
from models.review_result import ReviewResult


class GeneratorPromptBuilder:
    """
    Builds prompts for the Generator Agent.
    """

    @staticmethod
    def build(
        plan: ExecutionPlan,
        previous_review: ReviewResult | None = None,
    ) -> str:

        steps = "\n\n".join(
            f"{step.number}. {step.title}\n{step.description}"
            for step in plan.steps
        )

        files = "\n".join(
            plan.relevant_files
        )

        risks = "\n".join(
            f"- {risk}"
            for risk in plan.risks
        )

        if previous_review is None:

            review_feedback = """
No previous review exists.

This is the first implementation attempt.
"""

        else:

            issues = "\n".join(
                f"""
Severity: {issue.severity}
File: {issue.file}
Issue: {issue.description}
"""
                for issue in previous_review.issues
            )

            review_feedback = f"""
The previous implementation was rejected.

Summary

{previous_review.summary}

Issues Found

{issues}

Regenerate the implementation by fixing EVERY issue above.

Do NOT introduce new bugs.
Preserve all existing correct functionality.
"""

        prompt = f"""
You are an expert Senior Python Software Engineer.

Your responsibility is to implement the execution plan below.

==================================================
IMPORTANT RULES
==================================================

- Write production-quality Python code.
- Follow PEP 8.
- Reuse existing code whenever possible.
- Modify only the necessary files.
- Create new files only when absolutely necessary.
- Return COMPLETE file contents.
- Never return partial code.
- Never use TODO.
- Never use placeholders.
- Never use "...".
- Never use markdown.
- Never use ```python.
- Never use ```json.
- Never use Python triple quoted strings (\"\"\").
- Return ONLY valid JSON.
- The response MUST be parseable using Python json.loads().
- The "content" field MUST be a JSON string.
- Escape every newline using \\n.
- Escape every double quote using \\".
- The ONLY valid values for "action" are:
    - create
    - modify
- Never use:
    - new
    - update
    - edit

==================================================
Task
==================================================

{plan.task}

==================================================
Implementation Summary
==================================================

{plan.summary}

==================================================
Files To Modify
==================================================

{files}

==================================================
Implementation Steps
==================================================

{steps}

==================================================
Potential Risks
==================================================

{risks}

==================================================
Previous Review
==================================================

{review_feedback}

==================================================
Correct Example
==================================================

{{
    "summary": "Added JWT authentication",

    "files": [
        {{
            "path": "auth.py",
            "action": "modify",
            "content": "import jwt\\nfrom datetime import datetime\\n\\n\\ndef login():\\n    pass\\n"
        }}
    ]
}}

==================================================
Required JSON Format
==================================================

{{
    "summary": "Brief implementation summary",

    "files": [
        {{
            "path": "path/to/file.py",
            "action": "create",
            "content": "complete file contents"
        }},
        {{
            "path": "path/to/file.py",
            "action": "modify",
            "content": "complete file contents"
        }}
    ]
}}

==================================================
FINAL RULES
==================================================

- Return ONLY valid JSON.
- Do NOT return markdown.
- Do NOT explain your reasoning.
- Do NOT include any text before the JSON.
- Do NOT include any text after the JSON.
- Do NOT use triple quotes.
- Do NOT use code fences.
- The "content" field MUST be a valid JSON string.
- Escape newlines using \\n.
- Escape quotes using \\".
- Your entire response must be directly parsable by Python's json.loads().
"""

        return prompt