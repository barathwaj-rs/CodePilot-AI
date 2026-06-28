from models.final_report import FinalReport


class ReportFormatter:
    """
    Formats the final report into a readable string.
    """

    @staticmethod
    def format(report: FinalReport) -> str:

        status = "SUCCESS" if report.success else "FAILED"

        output = []

        output.append("=" * 60)
        output.append("            CodePilot AI Final Report")
        output.append("=" * 60)

        output.append("")
        output.append(f"Status : {status}")
        output.append(f"Task   : {report.task}")
        output.append(f"Retries: {report.retries}")

        output.append("")
        output.append("Summary")
        output.append("-" * 60)
        output.append(report.summary or "No summary provided.")

        output.append("")
        output.append("Generated Files")
        output.append("-" * 60)

        if report.generated_files:
            for file in report.generated_files:
                output.append(f"✓ {file}")
        else:
            output.append("None")

        output.append("")
        output.append("Remaining Issues")
        output.append("-" * 60)

        if report.issues:
            for issue in report.issues:
                output.append(
                    f"[{issue.severity.upper()}] "
                    f"{issue.file}: {issue.description}"
                )
        else:
            output.append("No issues.")

        output.append("")
        output.append("=" * 60)

        return "\n".join(output)