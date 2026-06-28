from models.final_report import FinalReport


class FinalReportBuilder:

    @staticmethod
    def build(state):

        generation = state["generation_result"]
        review = state["review_result"]

        return FinalReport(
            success=review.approved,
            task=state["user_task"],
            retries=state["retry_count"],
            summary=review.summary,
            generated_files=[
                file.path
                for file in generation.files
            ],
            issues=review.issues,
        )