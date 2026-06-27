from services.indexing.chunker import CodeChunker


text = """
class User:
    pass

class Product:
    pass

class Order:
    pass
""" * 200


chunks = CodeChunker.chunk(text)

print("Chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print("-" * 40)
    print(chunk[:150])