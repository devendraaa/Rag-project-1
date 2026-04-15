# src/utils/hash_registry.py
import hashlib
import json
import os

HASH_REGISTRY_PATH = "./data/vector_store/doc_hashes.json"  # ← matches your persist_directory

def compute_hash(text: str) -> str:
    """Generate MD5 hash for a text chunk."""
    return hashlib.md5(text.encode()).hexdigest()

def load_registry() -> dict:
    """Load existing hash registry from disk."""
    if os.path.exists(HASH_REGISTRY_PATH):
        with open(HASH_REGISTRY_PATH, "r") as f:
            return json.load(f)
    return {}

def save_registry(registry: dict):
    """Save updated hash registry to disk."""
    os.makedirs(os.path.dirname(HASH_REGISTRY_PATH), exist_ok=True)
    with open(HASH_REGISTRY_PATH, "w") as f:
        json.dump(registry, f, indent=2)

def filter_new_chunks(chunks: list) -> tuple:
    """
    Compare chunks against hash registry.
    Returns (new_chunks, updated_registry)
    """
    registry   = load_registry()
    new_chunks = []

    for chunk in chunks:
        content    = chunk.page_content
        source     = chunk.metadata.get("source", "unknown")
        page       = chunk.metadata.get("page", 0)
        chunk_id   = f"{source}_page{page}_{content[:40]}"  # unique & stable ID
        chunk_hash = compute_hash(content)

        if chunk_id in registry and registry[chunk_id] == chunk_hash:
            pass  # unchanged, skip silently
        else:
            new_chunks.append(chunk)
            registry[chunk_id] = chunk_hash  # register new/updated chunk

    return new_chunks, registry