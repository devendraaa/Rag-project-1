from langchain_core.documents import Document
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader, PyMuPDFLoader
from langchain_community.document_loaders import DirectoryLoader
import os
from src.utils.logger import get_logger

logger = get_logger(__name__)

os.makedirs("data/text_files", exist_ok=True)

# doc =  Document(
#     page_content="This is a test document for understanding document .",
#     metadata={
#                 "source": "test_document.txt",
#                 "author": "Devendra Chavan",
#                 "created_at": "2024-06-01"
#                 }   
#     )

# loader = TextLoader("data/text_files/python_intro.txt", encoding="utf-8")
# documents = loader.load()


#directory loader to load multiple files from a directory
# dir_loader = DirectoryLoader(
#             "data/text_files", 
#             glob="*.txt", #pattern to match files
#             loader_kwargs= {"encoding": "utf-8"},
#             show_progress=False
#             )
# documents = dir_loader.load()

def load_pdf():

    # pdf_loader = PyPDFLoader("data/pdf/sample.pdf")
    try:
        loader = DirectoryLoader(
            "data/pdf",
            glob="*.pdf",
            loader_cls=PyMuPDFLoader,
            show_progress=False  # or PyMuPDFLoader
        )
    
    except Exception as e:
        logger.error(f"Error loading PDF files: {e}")
        return []
    
    logger.info("PDF files loaded successfully.")
    pdf_data = loader.load()

    return pdf_data


