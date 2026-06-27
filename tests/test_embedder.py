from services.indexing.embedder import EmbeddingGenerator


def main():

    generator = EmbeddingGenerator()

    vectors = generator.embed([
        "def login(): pass",
        "class User: pass",
    ])

    print(f"Vectors: {len(vectors)}")
    print(f"Dimensions: {len(vectors[0])}")


if __name__ == "__main__":
    main()