from services.repository.tree_builder import TreeBuilder
from services.repository.entry_point_detector import EntryPointDetector


def main():

    files = TreeBuilder.build(".")

    entry_points = EntryPointDetector.detect(".", files)

    print("\nEntry Points\n")

    for entry in entry_points:
        print(entry)


if __name__ == "__main__":
    main()