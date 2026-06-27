from services.repository.tree_builder import TreeBuilder


def main():
    repo_path = "."  # Current project

    files = TreeBuilder.build(repo_path)

    print("\nRepository Files\n")

    for file in files:
        print(file)


if __name__ == "__main__":
    main()