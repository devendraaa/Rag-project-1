from src.retrival.retrival import RagRetrieval
# from src.llm_output.llm import test_llm
from src.vector_store.vector_store import VectorStore
from src.data_embedding.data_embed import EmbeddingModel
from src.llm_output.llm import rag_simple
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
import time
from src.utils.logger import get_logger

logger = get_logger(__name__)


def run_pipeline(query: str):
    try:
        start = time.time()
        logger.info("Loading query pipeline...")

        vector_store = VectorStore()
        logger.info("Vector store initialized.")

        emb = EmbeddingModel()
        logger.info("Embedding model initialized.")

        rag_retrival = RagRetrieval(vector_store=vector_store, embedding=emb)
        logger.info("RAG retrieval system initialized.")

        logger.info(f"Running RAG pipeline with query: '{query}'")

        groq_api_key = os.getenv("GROQ_API_KEY")
        if not groq_api_key:
            raise ValueError("GROQ_API_KEY not found")

        llm = ChatGroq(
            groq_api_key=groq_api_key,
            model="qwen/qwen3-32b",
            temperature=0.1,
            max_tokens=1024
        )

        response = rag_simple(
            query=query,
            ragRetrieval=rag_retrival,
            llm=llm,
            top_k=3
        )

        logger.info(f"Response generated (length={len(response)})")

        end = time.time()
        logger.info(f"Query took {end - start:.2f} seconds")

        return response

    except Exception as e:
        logger.error(f"Error running pipeline: {e}")
        raise e

