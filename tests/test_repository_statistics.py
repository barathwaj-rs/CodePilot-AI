from services.repository.tree_builder import TreeBuilder
from services.repository.repository_statistics import RepositoryStatistics


def main():

    files = TreeBuilder.build(".")

    stats = RepositoryStatistics.analyze(files)

    print(stats)


if __name__ == "__main__":
    main()