# 📚 Retrieval-Augmented Generation (RAG) Assistant

A Retrieval-Augmented Generation (RAG) application that enables users to chat with their own documents using Large Language Models (LLMs). The system converts uploaded documents into vector embeddings, stores them in a ChromaDB vector database, retrieves the most relevant context, and generates accurate, context-aware responses using Mistral AI.

Built with **LangChain**, **ChromaDB**, **Mistral AI**, and **Streamlit**.

---

## ✨ Features

- 📄 Load and process PDF and text documents
- 🔍 Semantic document retrieval using vector embeddings
- 🧠 Context-aware question answering
- ⚡ Fast similarity search with ChromaDB
- 💬 Interactive Streamlit interface
- 📚 Uses only retrieved document context to answer questions
- 🚫 Prevents hallucinations by grounding responses in source documents

---

## 🏗️ Architecture

```
                 Documents
          (PDF / TXT Files)
                    │
                    ▼
          Document Loader
                    │
                    ▼
             Text Splitter
                    │
                    ▼
          Embedding Generation
                    │
                    ▼
         ChromaDB Vector Store
                    │
             User Question
                    │
                    ▼
            Similarity Search
                    │
                    ▼
          Retrieved Context
                    │
                    ▼
             Mistral AI LLM
                    │
                    ▼
              Final Answer
```

---

## 🛠️ Tech Stack

### Programming Language

- Python

### Frameworks

- LangChain
- Streamlit

### Large Language Model

- Mistral AI

### Vector Database

- ChromaDB

### Embedding & Retrieval

- LangChain Embeddings
- Vector Similarity Search

### Document Processing

- PyPDF
- Text Loaders

---

## 📂 Project Structure

```
RAG-Project/
│
├── app.py
├── main.py
├── createDb.py
├── DB.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/officialadithya2005-maker/RAG-Project.git
```

Move into the project

```bash
cd RAG-Project
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=your_api_key
```

---

## ▶️ Run the Application

Launch the Streamlit interface

```bash
streamlit run app.py
```

---

## 🔄 Workflow

1. Load PDF or text documents.
2. Split documents into manageable chunks.
3. Generate embeddings for each chunk.
4. Store embeddings in ChromaDB.
5. Ask a question through the Streamlit interface.
6. Retrieve the most relevant document chunks.
7. Provide the retrieved context to Mistral AI.
8. Generate an accurate, context-aware response.

---

## 📸 Screenshots

Add screenshots of:

- Home Page
- Vector Database Creation
- Question Answering Interface
- Retrieved Context & Final Response

---

## 🎯 Use Cases

- Research paper assistant
- Technical documentation search
- Internal knowledge base chatbot
- Educational document assistant
- Personal document search

---

## 📈 Future Improvements

- Support for DOCX, PPTX, and HTML documents
- Conversation memory
- Multi-document collections
- Hybrid search (Keyword + Vector Search)
- Source citation highlighting
- Multi-model support (Gemini, OpenAI, Llama)
- Cloud deployment

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.
