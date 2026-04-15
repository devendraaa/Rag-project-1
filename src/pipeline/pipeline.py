from src.data_ingestion.data_ingest import load_pdf
from src.data_chunk.data_chunk import split_documents
from src.data_embedding.data_embed import EmbedingModel 
from src.vector_store.vector_store import VectorStore
from src.retrival.retrival import RagRetrieval
from src.llm_output.llm import test_llm

def run_pipeline():
    """Run the entire RAG pipeline: load data, chunk it, embed it, store it, and set up retrieval."""
    try:
        # Step 1: Load and chunk data
        print("Loading and chunking data...")

        documents = load_pdf()
        print(f"Data Loaded {len(documents)} documents from PDF.")
        chunks = split_documents(documents)
        print(f"Data chunked into {len(chunks)} chunks.")
        # print(f"Data chunked into {len(chunks)} chunks.")
        
        # Step 2: Embed chunks
        print("Embedding chunks...")
        embedding_model = EmbedingModel()
        texts = [chunk.page_content for chunk in chunks]
        embeddings = embedding_model.generate_embeddings(texts)
        print(f"Chunks embedded into vectors with shape: {embeddings.shape}")
        
        # Step 3: Store in vector database
        print("Storing embeddings in vector database...")
        vector_store = VectorStore()
        vector_store.add_documents(chunks, embeddings)
        
        # # Step 4: Set up retrieval
        # print("Setting up retrieval system...")
        # retriever = RagRetrieval(vector_store=vector_store)
        
        # print("Pipeline executed successfully!")
        # return retriever
    
        # print("Testing LLM with retrieval...")
        # output = test_llm(retriever)
        return chunks
    
    except Exception as e:
        print(f"Error running pipeline: {e}")
        raise e

