# PDF-RAG-System

An AI-powered PDF Retrieval System that extracts, processes, stores, and retrieves information from PDF documents using vector embeddings and semantic search.

## Overview

This project implements a Retrieval-Augmented Generation (RAG) pipeline for PDF documents. The system loads PDF files, extracts text, splits the content into manageable chunks, generates embeddings, stores them in a vector database, and performs similarity-based retrieval to find relevant information.

## Features

* PDF text extraction
* Text chunking and preprocessing
* Embedding generation using Sentence Transformers
* Vector storage using FAISS
* Semantic similarity search
* Fast and efficient document retrieval
* Modular Python implementation

## Project Structure

```text
PDF_Retrieval_Pipeline/
│
├── data/
│   └── sample.pdf
│
├── src/
│   ├── load_pdf.py
│   ├── split_text.py
│   ├── create_embeddings.py
│   └── similarity_search.py
│
├── vectorstore/
│
├── app.py
├── requirements.txt
└── README.md
```

## Technologies Used

* Python
* LangChain
* FAISS
* Sentence Transformers
* PyPDF
* Hugging Face Embeddings

## Installation

1. Clone the repository

```bash
git clone https://github.com/Priyavarshini13/PDF-RAG-System-.git
cd PDF-RAG-System-
```

2. Create a virtual environment

```bash
python -m venv venv
```

3. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Load PDF

```bash
python src/load_pdf.py
```

### Split Text

```bash
python src/split_text.py
```

### Create Embeddings

```bash
python src/create_embeddings.py
```

### Perform Similarity Search

```bash
python src/similarity_search.py
```

## Workflow

1. Upload or place PDF documents in the data folder.
2. Extract text from PDFs.
3. Split text into chunks.
4. Generate vector embeddings.
5. Store embeddings in FAISS.
6. Perform semantic search using user queries.
7. Retrieve the most relevant document chunks.

## Applications

* Document Question Answering
* Knowledge Base Search
* Research Paper Retrieval
* Enterprise Document Search
* Educational Content Retrieval

## Future Enhancements

* Conversational chatbot interface
* Multiple PDF support
* Web application using Streamlit
* LLM integration for answer generation
* Hybrid search and reranking

## Author

Priyavarshini V

## License

This project is intended for educational and learning purposes.
