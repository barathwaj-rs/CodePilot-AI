from graph.workflow import CodePilotWorkflow
from services.report.report_formatter import ReportFormatter

def main():

    workflow = CodePilotWorkflow().build()

    result = workflow.invoke(
        {
            "repo_url": ".",
            "user_task": "Add JWT Authentication",

            "retry_count": 0,
            

            "repo_analysis": None,
            "repository_context": None,
            "execution_plan": None,
            "generation_result": None,
            "review_result": None,
            "final_response": None,
            "git_branch": None,
            "git_commit": None,
        }
    )

    print("=" * 80)
    print("EXECUTION PLAN")
    print("=" * 80)
    print(result["execution_plan"])

    print()

    print("=" * 80)
    print("GENERATION RESULT")
    print("=" * 80)
    print(result["generation_result"])

    print()

    print("=" * 80)
    print("REVIEW RESULT")
    print("=" * 80)
    print(result["review_result"])

    print()

    print("=" * 80)
    print("FINAL REPORT")
    print("=" * 80)

    print(
    ReportFormatter.format(
        result["final_report"]
    )
    )


if __name__ == "__main__":
    main()