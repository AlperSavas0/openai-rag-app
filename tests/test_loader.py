from app.loader import load_pdf_text, chunk_text
from pathlib import Path

# Test for PDF text loading and chunking functions

def test_load_pdf_text_returns_string():
    example_pdf = Path("data/example.pdf")
    if not example_pdf.exists():
        # if test PDF does not exist, skip the test
        import pytest
        pytest.skip("Test PDF not found")
    text = load_pdf_text(str(example_pdf))
    assert isinstance(text, str)
    assert len(text) > 0

def test_chunk_text_returns_chunks():
    text = "Bu bir deneme metnidir. " * 50  # long text
    chunks = chunk_text(text)
    assert isinstance(chunks, list)
    assert all(isinstance(chunk, str) for chunk in chunks)
    assert len(chunks) > 1