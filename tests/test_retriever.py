from services.indexing.retriever import Retriever


def main():

    retriever = Retriever("CodePilot-AI")

    chunks = retriever.retrieve(
        "Where is repository analysis implemented?"
    )

    for chunk in chunks:

        print("=" * 80)
        print("File :", chunk.file)
        print("Score:", chunk.score)
        print(chunk.content[:200])


if __name__ == "__main__":
    main()