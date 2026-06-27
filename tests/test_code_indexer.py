from services.indexing.code_indexer import CodeIndexer


def main():

    indexer = CodeIndexer("CodePilot-AI")

    indexer.index_repository(".")


if __name__ == "__main__":
    main()