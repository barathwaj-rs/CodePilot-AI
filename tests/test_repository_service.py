from services.repository_service import RepositoryService


def main():

    repo = RepositoryService(
        "CodePilot-AI",
    )

    print(repo)


if __name__ == "__main__":
    main()