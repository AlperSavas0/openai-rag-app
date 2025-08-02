# Document Question Answering App

A lightweight Python application that allows users to upload a PDF document and ask questions about its content using OpenAI's GPT model and vector-based semantic search.

## Features

- Upload and process any Turkish-language PDF file
- Automatically extract and chunk the document content
- Use OpenAI Embeddings and FAISS for semantic search
- Retrieve top-k relevant text segments
- Generate context-aware answers with GPT-3.5-Turbo
- Clean Gradio interface for easy use

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/openai-rag-app.git
cd openai-rag-app
```

2. **Create and activate a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Add your OpenAI API key:**

Create a `.env` file in the root directory with the following line:

```env
OPENAI_API_KEY=your-api-key-here
```

## Usage

Run the Gradio interface with:

```bash
python app/interface.py
```

Then open your browser using the local URL provided in the terminal output.

## Structure

```
openai-rag-app/
├── app/
│   ├── loader.py           # PDF loading and text chunking
│   ├── retriever.py        # Embedding and FAISS logic
│   ├── llm.py              # LLM-based answer generation
│   └── interface.py        # Gradio interface
├── data/                   # Sample or user PDF uploads (ignored by git)
├── main.py                 # Test script for the pipeline 
├── requirements.txt
└── .env                    # Your API key (ignored by git)
```

## Notes

- Only Turkish PDF documents are supported for now.
- FAISS index is stored in-memory for real-time processing.
- Ensure your OpenAI API key has access to `gpt-3.5-turbo` and embedding endpoints.

---

Developed as a simple Retrieval-Augmented Generation (RAG) demo for document-based question answering.

