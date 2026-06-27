"""
Global configuration for CodePilot AI.
"""

# ===========================
# RAG
# ===========================

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

TOP_K_RESULTS = 5

# ===========================
# Embeddings
# ===========================

EMBEDDING_MODEL = "nomic-embed-text"

# ===========================
# ChromaDB
# ===========================

CHROMA_PATH = "./storage/chroma"

COLLECTION_PREFIX = "codepilot"

# ===========================
# Repository
# ===========================

SUPPORTED_EXTENSIONS = {
    ".py",
    ".md",
}