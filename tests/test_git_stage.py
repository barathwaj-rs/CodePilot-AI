from services.git.git_service import GitService


def main():

    repo = "."

    GitService.stage_all(repo)

    status = GitService.git_status(repo)

    print(status)


if __name__ == "__main__":
    main()