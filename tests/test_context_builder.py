from services.repository.analyzer import RepositoryAnalyzer
from services.rag.context_builder import ContextBuilder


def main():

    analysis = RepositoryAnalyzer.analyze(".")

    builder = ContextBuilder()

    context = builder.build(
        analysis,
        "Where is repository analysis implemented?",
    )

    print("Task:")
    print(context.user_task)

    print()

    print("Retrieved Files:")

    for chunk in context.retrieved_chunks:
        print("-", chunk.file)


if __name__ == "__main__":
    main()