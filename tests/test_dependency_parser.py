from services.repository.tree_builder import TreeBuilder
from services.repository.dependency_parser import DependencyParser


def main():

    files = TreeBuilder.build(".")

    dependencies = DependencyParser.parse(".", files)

    print("\nDependencies\n")

    for language, packages in dependencies.items():

        print(language)

        for package in packages:
            print(f"  - {package}")


if __name__ == "__main__":
    main()