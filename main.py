from src.pipeline.query_pipeline import run_pipeline
from src.utils.logger import setup_logging, get_logger

if __name__ == "__main__":
    # ✅ Initialize logging FIRST
    setup_logging()
    
    logger = get_logger(__name__)

    logger.info("Application started")

    response = run_pipeline(query="What is layer normalization?")

    logger.info("Pipeline executed successfully")
    logger.info(f"Response: {response}")

    print("pipeline executed successfully!")
    print(f"Response: {response}")