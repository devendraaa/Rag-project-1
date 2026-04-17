from fastapi import FastAPI
from pydantic import BaseModel
from src.pipeline.query_pipeline import run_pipeline
from logging import getLogger

logger = getLogger(__name__)

app = FastAPI(title="RAG Agentic AI API", version="1.0")

# request schema
class QueryRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "Welcome to the RAG Agentic AI API!"}

@app.post("/query")
def query_rag(request: QueryRequest):
    try:
        logger.info(f"Received query: {request.query}")

        response = run_pipeline(request.query)

        return {
            "query": request.query,
            "response": response
        }

    except Exception as e:
        logger.error(f"Error: {e}")
        return {"error": str(e)}