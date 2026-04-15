from langchain_text_splitters import RecursiveCharacterTextSplitter
from pymupdf import Document
from src.config.seting import CHUNK_SIZE, CHUNK_OVERLAP
# from src.data_ingestion.data_ingest import load_pdf
from src.utils.logger import get_logger

logger = get_logger(__name__)

def split_documents(documents, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP):
    
    """ Split documents into smaller chunks
    Args:
        documents: List of Document objects or raw strings.
        chunk_size: Max characters per chunk.
        chunk_overlap: Overlap between chunks.
    Returns:
        List of Document chunks
    """
    
    # Ensure all inputs are Document objects
    if isinstance(documents[0], str):
        documents = [Document(page_content=doc, metadata={}) for doc in documents]

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=['\n\n', '\n', ' ', '']
    )
    
    split_docs = text_splitter.split_documents(documents)
    logger.info(f"Split {len(documents)} documents into {len(split_docs)} chunks")
    # logger.info(f"Split {len(documents)} documents into {len(split_docs)} chunks")

    # show example of chunk
    if split_docs:
        logger.info(f"\n Example chunk")
        logger.info(f"Content : {split_docs[0].page_content[:200]}...")
        logger.info(f"Metadata : {split_docs[0].metadata}")
    
    return split_docs