from services.git.git_service import GitService


def main():

    repo = "."

    hash_value = GitService.commit(
        repo,
        "Test commit from CodePilot AI",
    )

    print("Commit Hash:")
    print(hash_value)

    print()

    print("Latest Commit:")
    print(
        GitService.latest_commit(
            repo,
        )
    )


if __name__ == "__main__":
    main()