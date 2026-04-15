import os
import uuid
import chromadb
from chromadb.config import Settings
from langchain_core.documents import Document
# from src.data_embedding.data_embed import text_to_embeddings
import numpy as np

class VectorStore:
    """ A simple vector store implementation using chomadb for storing and retrieving document embeddings"""
    def __init__(self, collection_name: str = "pdf_documents", persist_directory: str = "data/vector_store"):
        """Initialize the vector store

        Args:
            collection_name: name of the collection to store embeddings
            persist_directory: directory to persist the vector store
        """
        self.collection_name = collection_name
        self.persist_directory = persist_directory
        self.client = None
        self.collection = None
        self._initialize_store()
    
    def _initialize_store(self):
        """Initialize the ChromaDB client and collection"""
        try:
            #create presist directory if it doesn't exist
            os.makedirs(self.persist_directory, exist_ok=True)
            self.client = chromadb.PersistentClient(path = self.persist_directory)

            #get create collection
            self.collection = self.client.get_or_create_collection(
                name=self.collection_name,
                metadata={"description": "Collection of PDF document embeddings"}
                )
            print(f"Vector store initialized with collection '{self.collection_name}' at '{self.persist_directory}'")

        except Exception as e:
            print(f"Error initializing vector store: {e}")
            raise e
    
    def add_documents(self, documents: list[Document], embeddings: np.ndarray):
        """add documents and their corresponding embeddings to the vector store"""
        if len(documents) != len(embeddings):
            raise ValueError("The number of documents and embeddings must be the same.")
        print(f"Adding {len(documents)} documents to the vector store...")

        #prepare data for chromadb
        ids = []
        metadatas = []
        documments_text = []
        embedding_list = []

        for i, (doc, embedding) in enumerate(zip(documents, embeddings)):
            doc_id = str(uuid.uuid4())  # generate unique id for each document
            ids.append(doc_id)

            #prepare metadata for chromadb, ensure it's a dict

            metadata = dict(doc.metadata)  # convert metadata to dict if it's not already
            metadata['doc_index'] = i
            metadata['content_length'] = len(doc.page_content)
            metadatas.append(metadata)

            #document content
            documments_text.append(doc.page_content)
            embedding_list.append(embedding.tolist())  # convert numpy array to list for chromadb
        #add to chromadb collection
        try:
            self.collection.add(
                ids=ids,
                metadatas=metadatas,
                documents=documments_text,
                embeddings=embedding_list
            )
            print(f"Successfully added {len(documents)} documents to the vector store.")
            print(f"total documents in collection: {self.collection.count()}")

        except Exception as e:
            print(f"Error adding documents to vector store: {e}")
            raise e
