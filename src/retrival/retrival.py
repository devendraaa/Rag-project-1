import os
import uuid
import numpy as np
from typing import List, Dict, Any
from langchain_core.documents import Document
from src.vector_store.vector_store import VectorStore
from src.data_embedding.data_embed import EmbeddingModel


class RagRetrieval:
    """handles query-base retrieval from the vector store"""
    def __init__(self, vector_store: VectorStore, embedding: EmbeddingModel):
        """initialize the retrieval class with vector store and embedding model
        Args:
            vector_store: instance of the VectorStore class for retrieving document embeddings
            embedding: instance of the EmbeddingModel class for generating query embeddings
        """
        self.vector_store = vector_store
        self.embedding = embedding
    
    def retrieve(self, query: str, top_k: int = 5, score_threshold: float = 0.0) -> List[Dict[str, Any]]:
        """retrieve relevant documents based on the query
        Args:
            query: input query string for retrieval
            top_k: number of top relevant documents to retrieve
            score_threshold: minimum cosine similarity score for retrieved documents
        Returns:
            List of retrieved documents with their metadata and similarity scores
        """
        print(f"Retrieving documents for query: '{query}'")
        print("Generating embedding for the query...")
        print(F"TOP_K: {top_k}, SCORE_THRESHOLD: {score_threshold}")

        # GENERATE QUERY EMBEDDING
        query_embedding = self.embedding.embed_documents([query])[0]  # get the embedding for the query
        print("Query embedding generated.")

        # search in vector store
        try:
            results = self.vector_store.collection.query(
                query_embeddings=[query_embedding.tolist()],
                n_results=top_k
            )

            # process results and filter based on score threshold
            retrieved_docs = []

            if results['documents'] and results['documents'][0]:  # check if there are any results
                documents = results['documents'][0]
                metadatas = results['metadatas'][0]
                distances = results['distances'][0]
                ids = results['ids'][0]

                for i, (doc_id, documents, metadatas, distance) in enumerate(zip(ids, documents, metadatas, distances)):
                    #convert distance to similarity score (assuming distance is cosine distance, similarity = 1 - distance)
                    similarity_score = 1 - distance  # convert distance to similarity score
                    if similarity_score >= score_threshold:
                        retrieved_docs.append({
                            "id": doc_id,
                            "content": documents,
                            "metadata": metadatas,
                            "similarity_score": similarity_score,
                            "distance": distance,
                            "rank": i + 1
                        })
                print(f"Retrieved {len(retrieved_docs)} documents that meet the score threshold.")
            else:
                print("No documents retrieved from the vector store.")

            return retrieved_docs
        
        except Exception as e:
            print(f"Error retrieving documents: {e}")
            raise e
        
# ragRetrieval=RagRetrieval(vector_store=Vectorstore, embedding=embedding_manager)

# def retrive_doc():
#     try:
#         vec = VectorStore()
#         emb = EmbedingModel()
#         rag_retrival = RagRetrieval(vector_store=vec, embedding=emb)
#         print("RAG Retrieval instance created successfully.")
#         return rag_retrival
#     except Exception as e:
#         print(f"Error creating RAG Retrieval instance: {e}")
#         raise e
