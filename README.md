# LangChain Document Agent

A Retrieval-Augmented Generation (RAG) application built using LangChain, FAISS, HuggingFace Embeddings, and Gemini.

The application ingests PDF documents, creates semantic embeddings, stores them in a FAISS vector database, and retrieves relevant information to answer user questions.

## Features

* PDF document ingestion
* Text chunking using RecursiveCharacterTextSplitter
* Semantic embeddings using Sentence Transformers
* FAISS vector database for similarity search
* Retrieval-Augmented Generation (RAG)
* Gemini-powered question answering
* Modular project structure
* Streamlit UI (Work in Progress)

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
Similarity Search
      |
      v
Gemini LLM
      |
      v
Final Answer
```

---

## Project Structure

```text
langchain-document-agent/
│
├── app.py
├── README.md
├── .env.example
├── data/
├── tests/
│
└── src/
    ├── config.py
    ├── ingest.py
    ├── embeddings.py
    ├── vector_store.py
    └── rag.py
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

Activate virtual environment:

```bash
poetry shell
```

---

## Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

Never commit the `.env` file to GitHub.

Example template:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## Running Tests

PDF ingestion:

```bash
poetry run python tests/test_pdf.py
```

Chunking:

```bash
poetry run python tests/test_chunking.py
```

Embeddings:

```bash
poetry run python tests/test_embeddings.py
```

Vector Search:

```bash
poetry run python tests/test_faiss.py
```

---

## Example Queries

* What is the remote work policy?
* What is the vacation policy?
* What are the product specifications?
* What is the recommended chunk size for RAG?
* What security requirements are mentioned?

---

## Technologies Used

* Python
* LangChain
* FAISS
* Sentence Transformers
* Gemini
* Poetry
* Streamlit

---

## Future Enhancements

* Multi-document support
* Conversational memory
* Agent-based tool selection
* CSV analysis
* Hybrid search (BM25 + Vector Search)
* Streamlit UI
* Deployment on Cloud

---

## Learning Goals

This project was built to understand:

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Databases
* Embeddings
* LangChain Components
* AI Agent Development
