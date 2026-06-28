from services.apply_changes.apply_service import ApplyChangesService


def apply_changes(state):

    if state is None:
        return (
            "No generated workflow found.\n"
            "Please click Generate first."
        )

    if not state["review_result"].approved:
        return (
            "❌ Changes cannot be applied.\n\n"
            "The generated code was not approved."
        )

    try:
        ApplyChangesService.apply(state)

    except Exception as e:
        return f"❌ {e}"

    output = []

    output.append("✅ Changes applied successfully.")
    output.append("")

    if state.get("git_branch"):
        output.append(f"Branch : {state['git_branch']}")

    if state.get("git_commit"):
        output.append(f"Commit : {state['git_commit']}")

    if state.get("commit_message"):
        output.append(f"Message: {state['commit_message']}")

    return "\n".join(output)