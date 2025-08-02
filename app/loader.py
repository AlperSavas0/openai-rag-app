import fitz # PyMuPDF
from typing import List
from pathlib import Path

def load_pdf_text(file_path: str) -> str:
    """
    Load text from a PDF file.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF.
    """
    pdf_document = fitz.open(file_path)
    text = ""
    
    for page in pdf_document:
        text += page.get_text()
    
    pdf_document.close()
    return text

def chunk_text(text: str, chunk_size: int = 1000, overlap: int =200) -> List[str]:
    """
    Split text into chunks of a specified size.

    Args:
        text (str): The text to be split into chunks.
        chunk_size (int): The maximum size of each chunk.
        overlap (int): The number of overlapping characters between chunks.

    Returns:
        List[str]: A list of text chunks.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

if __name__ == "__main__":
    # Example usage
    example_pdf_path = "data/example.pdf"  # Replace with your PDF file path
    
    if Path(example_pdf_path).exists():
        raw_text = load_pdf_text(example_pdf_path)
        chunks= chunk_text(raw_text)
        
        print(f"Dosya bulundu: {example_pdf_path}")
        print(f"Toplam karakter: {len(raw_text)}")
        print(f"Chunk sayısı: {len(chunks)}")
        print("İlk chunk:")
        print(chunks[0])
    else:
        print(f"File {example_pdf_path} does not exist.")