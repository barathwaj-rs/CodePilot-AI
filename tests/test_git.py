from services.git.git_service import GitService


def main():

    repo = "."

    branch = "codepilot-test"

    print(
        "Is Git Repository:",
        GitService.is_git_repository(repo),
    )

    print(
        "Current Branch:",
        GitService.current_branch(repo),
    )

    GitService.create_branch(
        repo,
        branch,
    )

    print(
        "Branch Exists:",
        GitService.branch_exists(
            repo,
            branch,
        ),
    )

    GitService.checkout_branch(
        repo,
        branch,
    )

    print(
        "Current Branch:",
        GitService.current_branch(repo),
    )

    print()

    print(
        "Repository Clean:",
        GitService.is_clean(repo),
    )

    print()

    print("Git Status:")

    status = GitService.git_status(repo)

    print(status)


if __name__ == "__main__":
    main()