from models.repository_context import RepositoryContext


class PlannerPromptBuilder:
    """
    Builds prompts for the Planner Agent.
    """

    @staticmethod
    def build(
        context: RepositoryContext,
    ) -> str:

        # -----------------------------
        # Repository Information
        # -----------------------------

        languages = "\n".join(
            f"- {language}: {count} files"
            for language, count in context.analysis.languages.items()
        )

        frameworks = (
            "\n".join(context.analysis.frameworks)
            if context.analysis.frameworks
            else "None"
        )

        dependencies = []

        for language, packages in context.analysis.dependencies.items():

            dependencies.append(f"{language}:")

            for package in packages:
                dependencies.append(f"  - {package}")

        dependencies = (
            "\n".join(dependencies)
            if dependencies
            else "None"
        )

        entry_points = (
            "\n".join(context.analysis.entry_points)
            if context.analysis.entry_points
            else "None"
        )

        # -----------------------------
        # Retrieved Code
        # -----------------------------

        if context.retrieved_chunks:

            retrieved_code = "\n\n".join(
                f"""
File:
{chunk.file}

Score:
{chunk.score:.3f}

Code:
{chunk.content}
""".strip()
                for chunk in context.retrieved_chunks
            )

        else:

            retrieved_code = "No relevant code retrieved."

        # -----------------------------
        # Final Prompt
        # -----------------------------

        prompt = f"""
You are an expert Senior Software Architect.

Your responsibility is to create a detailed implementation plan.

IMPORTANT RULES

- Do NOT write code.
- Think step-by-step.
- Analyze the repository carefully.
- Suggest only implementation steps.
- Return ONLY valid JSON.
- Do NOT include markdown.

==================================================
Repository Information
==================================================

Languages
---------
{languages}

Frameworks
----------
{frameworks}

Dependencies
------------
{dependencies}

Entry Points
------------
{entry_points}

==================================================
Relevant Code
==================================================

{retrieved_code}

==================================================
User Task
==================================================

{context.user_task}

==================================================
Required JSON Format
==================================================

{{
    "summary": "Brief summary of the implementation plan",

    "relevant_files": [
        "file1.py",
        "file2.py"
    ],

    "steps": [
        {{
            "number": 1,
            "title": "Step title",
            "description": "Detailed explanation"
        }}
    ],

    "risks": [
        "Possible issue 1",
        "Possible issue 2"
    ]
}}

Return ONLY valid JSON.
"""

        return prompt