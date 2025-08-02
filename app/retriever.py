from typing import List
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.docstore.document import Document
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

embedding_model= OpenAIEmbeddings(openai_api_key=openai_api_key)

faiss_index= None

def create_faiss_index(chunks: list[str]) -> None:
    """
    Create an in-memory FAISS index from a list of text chunks.

    Args:
        chunks (List[str]): List of text chunks to index.
    """
    
    global faiss_index
    documents = [Document(page_content=chunk) for chunk in chunks]
    
    faiss_index = FAISS.from_documents(documents, embedding_model) 
        
   
    
def get_similar_chunks(query: str, k: int = 8) -> List[str]:
    """
    Retrieve top-k similar chunks from the in-memory FAISS index for a given query.

    Args:
        query (str): The user question.
        k (int): Number of similar chunks to retrieve.

    Returns:
        List[str]: List of most relevant chunk texts.
    """
    
    global faiss_index
    if faiss_index is None:
        raise FileNotFoundError(f"FAISS index not created. Please create the index first.")
        
    results = faiss_index.similarity_search(query, k=k)
    return [doc.page_content for doc in results]
