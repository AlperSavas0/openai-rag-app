from app.retriever import create_faiss_index, get_similar_chunks
import os

# Test for creating FAISS index and retrieving relevant chunks

def test_faiss_index_and_retrieval():
    chunks = [
        "Bu belge yapay zeka konularını ele almaktadır.",
        "Gradio arayüzü, PDF belgelerini işler.",
        "OpenAI API anahtarı gereklidir."
    ]
    create_faiss_index(chunks)
    results = get_similar_chunks("Yapay zeka hakkında ne diyor?")
    assert isinstance(results, list)
    assert len(results) > 0
    assert any("yapay zeka" in res.lower() for res in results)