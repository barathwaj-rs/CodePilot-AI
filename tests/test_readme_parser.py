from services.repository.readme_parser import ReadmeParser


def main():

    readme = ReadmeParser.parse(".")

    print(readme)


if __name__ == "__main__":
    main()