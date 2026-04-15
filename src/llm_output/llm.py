from dotenv import load_dotenv
from sympy import content
load_dotenv()
from src.utils.logger import get_logger

logger = get_logger(__name__)

# simple rag function : retrieve relevant documents and generate response using llm
def rag_simple(query: str, ragRetrieval, llm, top_k=3):
    """Simple RAG function to retrieve relevant documents and generate response using LLM
    Args:
        query: input query string for retrieval and response generation
        ragRetrieval: instance of the RagRetrieval class for retrieving relevant documents
        llm: instance of the ChatGroq class for generating response
        top_k: number of top relevant documents to retrieve
        score_threshold: minimum cosine similarity score for retrieved documents"""
    results = ragRetrieval.retrieve(query=query, top_k=top_k)
    context = "\n\n".join([doc['content'] for doc in results]) if results else "No relevant results found."
    if not content:
        logger.warning("No relevant documents found for the query.")
        return "No relevant documents found to answer the query."
    #generate response using llm
    # prompt = f"Use the following retrieved documents to answer the question:\n\n{context}\n\nQuestion: {query}\nAnswer:"
    prompt = f"""
            You are an expert AI assistant.

            Answer the question using ONLY the provided context.

            Rules:
            - Do not use outside knowledge
            - If answer is not present, say "I don't know based on the context"
            - Keep answer clear and concise

            Context:
            {context}

            Question:
            {query}

            Answer:
            """
    response = llm.invoke([prompt.format(context=context, query=query)])
    return response.content

# def test_llm():
#     try:
#         rag_retrieval = retrieve_doc()
#         query = "What are the key findings from the document regarding the impact of climate change on agriculture?"
#         response = rag_simple(query=query, ragRetrieval=rag_retrieval, llm=llm, top_k=3)
#         logger.info("Response from LLM:")
#         logger.info(response)
#     except Exception as e:
#         logger.error(f"Error during LLM test: {e}")
#         raise e