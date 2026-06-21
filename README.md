# LangChain Document Agent

An Agentic Retrieval-Augmented Generation (RAG) application built using LangChain, FAISS, HuggingFace Embeddings, Ollama, and Qwen.

The application ingests PDF documents, creates semantic embeddings, stores them in a FAISS vector database, retrieves relevant information, and uses an LLM-powered agent to select the appropriate tool for answering user requests.

---

## Features

* PDF document ingestion
* Recursive text chunking
* Semantic search using Sentence Transformers
* FAISS vector database
* Metadata-aware retrieval
* Source attribution
* Local LLM inference using Qwen (Ollama)
* Agent-based tool routing
* Specialized tools for:

  * Document Question Answering
  * Document Summarization
  * Source Listing
  * Event Extraction
* Modular project structure
* Streamlit UI (Planned)

---

## Architecture

```text
PDF Document
      |
      v
Text Extraction
      |
      v
Chunking
      |
      v
Embeddings
      |
      v
FAISS Vector Store
      |
      v
Metadata Retrieval
      |
      v
Qwen Agent Router
      |
      +---------------------------+
      |                           |
      v                           v
search_document         summarize_document
      |
      +---------------------------+
      |                           |
      v                           v
list_sources             upcoming_events
      |
      v
Final Response
```

---

## Project Structure

```text
langchain-document-agent/
│
├── app.py
├── README.md
├── .env.example
├── pyproject.toml
│
├── data/
│   └── sample.pdf
│
├── faiss_index/
│   ├── index.faiss
│   └── index.pkl
│
├── tests/
│   ├── test_pdf.py
│   ├── test_chunking.py
│   ├── test_embeddings.py
│   ├── test_faiss.py
│   ├── test_rag.py
│   ├── test_qwen.py
│   └── test_agent.py
│
└── src/
    ├── ingest.py
    ├── embeddings.py
    ├── vector_store.py
    ├── rag.py
    ├── llm.py
    ├── pipeline.py
    ├── tools.py
    └── agent_qwen.py
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/7pandeys/langchain-document-agent.git

cd langchain-document-agent
```

Install dependencies:

```bash
poetry install
```

Activate environment:

```bash
poetry shell
```

---

## Local LLM Setup (Ollama)

Install Ollama:

```bash
brew install ollama
```

Start Ollama:

```bash
ollama serve
```

Pull Qwen:

```bash
ollama pull qwen
```

Verify:

```bash
ollama list
```

---

## Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

Note:

* Gemini was used during early development.
* Current implementation uses local Qwen through Ollama.
* API keys should never be committed to GitHub.

Create `.env.example`:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## Running Tests

### PDF Ingestion

```bash
poetry run python tests/test_pdf.py
```

### Chunking

```bash
poetry run python tests/test_chunking.py
```

### Embeddings

```bash
poetry run python tests/test_embeddings.py
```

### Vector Search

```bash
poetry run python tests/test_faiss.py
```

### RAG Pipeline

```bash
poetry run python tests/test_rag.py
```

### Qwen LLM

```bash
poetry run python tests/test_qwen.py
```

### Agentic RAG

```bash
poetry run python tests/test_agent.py
```

---

## Agent Tools

### search_document

Answers questions using Retrieval-Augmented Generation (RAG).

Example:

```text
What is the vacation policy?
What products are available?
```

---

### summarize_document

Generates a high-level summary of the document.

Example:

```text
Summarize the document.
```

---

### list_sources

Returns source documents and page references.

Example:

```text
Show document sources.
```

---

### upcoming_events

Extracts events, workshops, meetings and dates.

Example:

```text
What upcoming events are scheduled?
```

---

## Metadata Support

Each chunk contains metadata:

```python
{
    "source": "data/sample.pdf",
    "page": 1,
    "version": "v1"
}
```

Benefits:

* Source attribution
* Explainability
* Auditing
* Future document versioning
* Metadata filtering

---

## Example Queries

```text
What is the remote work policy?

What is the vacation policy?

List the products.

Summarize the document.

Show document sources.

What upcoming events are scheduled?
```

---

## Technologies Used

* Python
* LangChain
* FAISS
* HuggingFace Embeddings
* Sentence Transformers
* Ollama
* Qwen
* Poetry
* Streamlit (Planned)

---

## Future Enhancements

* Multi-document support
* Hybrid Search (BM25 + Vector Search)
* Retrieval Re-ranking
* Document Versioning
* LangGraph Integration
* Qdrant Vector Database
* Streamlit UI
* Cloud Deployment
* Evaluation Framework

---

## Learning Outcomes

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Embeddings
* Vector Databases
* Metadata-Based Retrieval
* Source Attribution
* Agentic AI
* Tool Routing
* Local LLM Deployment
* LangChain Development

---

## Author

Sandeep Pandey

GitHub:
https://github.com/7pandeys

Learning Journey:

Data Engineering → AI Engineering → Agentic AI → LangGraph
