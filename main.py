from app.loader import load_pdf_text, chunk_text
from app.retriever import create_faiss_index, get_similar_chunks
from app.llm import get_answer
from pathlib import Path

# This script is for testing the document processing pipeline without using the Gradio interface.
# It loads a sample PDF, creates a FAISS index, and queries it with a sample question.

# Path to the example PDF
example_pdf_path = "data/example.pdf"

# Check if the PDF file exists
if not Path(example_pdf_path).exists():
    print(f"PDF not found: {example_pdf_path}")
    exit()

# 1. Read the PDF file
print("Reading PDF...")
raw_text = load_pdf_text(example_pdf_path)

# 2. Split the text into smaller chunks
chunks = chunk_text(raw_text)
print(f"{len(chunks)} chunks created.")

# 3. Create embeddings and save to FAISS vector database
print("Generating embeddings and saving to FAISS...")
create_faiss_index(chunks)

# 4. Define a sample user question
question = "What is the purpose of this document?"

# 5. Retrieve the most relevant chunks using the question
print(f"Question: {question}")
similar_chunks = get_similar_chunks(question)

# 6. Get an answer from the LLM using the relevant chunks
answer = get_answer(question, similar_chunks)

# 7. Print the answer
print("\nAnswer:")
print(answer)
