import numpy as np
from typing import List
from src.config.seting import MODEL_NAME
from src.utils.logger import get_logger

logger = get_logger(__name__)

class EmbeddingModel:
    """Handles document embedding generation using SentenceTransformer"""

    _model = None

    def __init__(self, model_name: str = MODEL_NAME):
        self.model_name = model_name

        if EmbeddingModel._model is None:
            self._load_model()
            EmbeddingModel._model = self.model
        else:
            self.model = EmbeddingModel._model

        logger.info(f"Embedding model '{self.model_name}' initialized successfully.")

    def _load_model(self):
        try:
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer(self.model_name)
            logger.info(f"Model '{self.model_name}' loaded successfully.")
            logger.info(f"Embedding dimension: {self.model.get_embedding_dimension()}")
        except Exception as e:
            logger.error(f"Error loading model '{self.model_name}': {e}")
            raise e

    def embed_documents(self, texts: List[str]) -> np.ndarray:
        if self.model is None:
            raise ValueError("Model not loaded.")

        try:
            logger.info(f"Generating embeddings for {len(texts)} texts...")
            embeddings = self.model.encode(texts, show_progress_bar=False)
            logger.info(f"Embeddings shape: {embeddings.shape}")
            return embeddings

        except Exception as e:
            logger.error(f"Error generating embeddings: {e}")
            raise e