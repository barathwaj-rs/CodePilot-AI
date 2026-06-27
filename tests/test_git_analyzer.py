from services.repository.git_analyzer import GitAnalyzer


def main():

    info = GitAnalyzer.analyze(".")

    print(info)


if __name__ == "__main__":
    main()