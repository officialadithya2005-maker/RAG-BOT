import os
import shutil
import tempfile

import streamlit as st
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

st.set_page_config(
    page_title="PDF RAG Assistant",
    page_icon="📄",
    layout="wide"
)

st.title("📄 PDF RAG Assistant")

st.write("Upload a PDF and chat with it.")

# ================= Sidebar ================= #

st.sidebar.title("Settings")

uploaded_file = st.sidebar.file_uploader(
    "Upload PDF",
    type="pdf"
)

storage_mode = st.sidebar.radio(
    "Vector Database",
    [
        "Memory Database",
        "Persistent Database"
    ]
)

# ================= Session State ================= #

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "processed_file" not in st.session_state:
    st.session_state.processed_file = None

# ================= Process Button ================= #

if uploaded_file:

    if st.sidebar.button("Create Vector Database"):

        with st.spinner("Processing PDF..."):

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".pdf"
            ) as temp_pdf:

                temp_pdf.write(uploaded_file.read())
                pdf_path = temp_pdf.name

            loader = PyPDFLoader(pdf_path)

            docs = loader.load()

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )

            chunks = splitter.split_documents(docs)

            embeddings = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )

            if storage_mode == "Persistent Database":

                if os.path.exists("chroma_db"):
                    shutil.rmtree("chroma_db")

                vectorstore = Chroma.from_documents(
                    documents=chunks,
                    embedding=embeddings,
                    persist_directory="chroma_db"
                )

            else:

                vectorstore = Chroma.from_documents(
                    documents=chunks,
                    embedding=embeddings
                )

            st.session_state.vectorstore = vectorstore
            st.session_state.processed_file = uploaded_file.name

            os.remove(pdf_path)

        st.sidebar.success("Vector Database Created!")

        st.sidebar.write(f"Pages : {len(docs)}")
        st.sidebar.write(f"Chunks : {len(chunks)}")

# ================= Chat ================= #

if st.session_state.vectorstore is not None:

    retriever = st.session_state.vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 4,
            "fetch_k": 10,
            "lambda_mult": 0.5
        }
    )

    llm = ChatMistralAI(
        model="mistral-small-2506"
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer is not found in the context, say:

"I could not find the answer in the uploaded PDF."

Context:
{context}
"""
            ),
            (
                "human",
                "{question}"
            )
        ]
    )

    for role, message in st.session_state.chat_history:

        with st.chat_message(role):
            st.markdown(message)

    question = st.chat_input(
        "Ask a question..."
    )

    if question:

        st.session_state.chat_history.append(
            ("user", question)
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.spinner("Thinking..."):

            docs = retriever.invoke(question)

            context = "\n\n".join(
                doc.page_content
                for doc in docs
            )

            final_prompt = prompt.invoke(
                {
                    "context": context,
                    "question": question
                }
            )

            response = llm.invoke(final_prompt)

        with st.chat_message("assistant"):
            st.markdown(response.content)

        st.session_state.chat_history.append(
            ("assistant", response.content)
        )

else:

    st.info(
        "Upload a PDF, choose the database type and click **Create Vector Database**."
    )