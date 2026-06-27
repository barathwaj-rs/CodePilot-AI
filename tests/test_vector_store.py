from services.indexing.embedder import EmbeddingGenerator
from services.indexing.vector_store import VectorStore


def main():

    texts = [
        "def login(): pass",
        "class User: pass",
        "def register(): pass",
    ]

    generator = EmbeddingGenerator()

    embeddings = generator.embed(texts)

    store = VectorStore()

    store.add(
        documents=texts,
        embeddings=embeddings,
        metadatas=[
            {"file": "auth.py"},
            {"file": "user.py"},
            {"file": "register.py"},
        ],
        ids=[
            "chunk_login",
            "chunk_user",
            "chunk_register",
        ],
    )

    query = generator.embed(["login function"])[0]

    results = store.search(query)

    print(results)
    

if __name__ == "__main__":
    main()