import streamlit as st
if "messages" not in st.session_state:
    st.session_state.messages = []
from document_loader import load_pdf , load_docx , load_pptx , load_txt
from utils import split_text
from embeddings import create_embeddings
from vector_db import store_chunks
from rag import ask_rag

st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="📄"
)
st.title("📄 AI Document Assistant")

with st.sidebar:
    st.header("📂 Upload Document")
    uploaded_files = st.file_uploader (
        "Choose a document",
        type=["pdf", "docx", "pptx" , "txt"],
        accept_multiple_files=True
    )
    st.markdown("---")
    st.info("Ask questions about your uploaded document.")
    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

if uploaded_files:

    all_chunks = []
    all_embeddings = []
    all_metadatas = []

    for uploaded_file in uploaded_files:

        filename = uploaded_file.name.lower()
        filepath = f"documents/{uploaded_file.name}"

        with open(filepath, "wb") as f:
            f.write(uploaded_file.getbuffer())

        if filename.endswith(".pdf"):
            text = load_pdf(filepath)

        elif filename.endswith(".docx"):
            text = load_docx(filepath)

        elif filename.endswith(".pptx"):
            text = load_pptx(filepath)

        elif filename.endswith(".txt"):
            text = load_txt(filepath)

        else:
            continue

        print(f"{uploaded_file.name} Text Length:", len(text))

        chunks = split_text(text)

        if len(chunks) == 0:
            continue

        embeddings = create_embeddings(chunks)

        all_chunks.extend(chunks)
        all_embeddings.extend(embeddings)

        for _ in chunks:
            all_metadatas.append(
                {
                    "filename": uploaded_file.name
                }
            )

    if len(all_chunks) == 0:
        st.error("❌ No readable text found in the uploaded documents.")
        st.stop()

    print("Total Chunks:", len(all_chunks))
    print("Total Embeddings:", len(all_embeddings))
    print("Total Metadata:", len(all_metadatas))

    store_chunks(
        all_chunks,
        all_embeddings,
        all_metadatas
    )

    st.success(f"✅ {len(uploaded_files)} document(s) processed successfully!")

    question = st.chat_input("Ask a question ...")

    if question:

        with st.spinner("🤖 Thinking..."):
            answer, sources , metadatas = ask_rag(question)

        st.session_state.messages.append(
            {
                "question": question,
                "answer": answer,
                "sources": sources,
                "metadatas": metadatas
            }
        )

    for chat in st.session_state.messages:

        with st.chat_message("user"):
            st.write(chat["question"])

        with st.chat_message("assistant"):
            st.write(chat["answer"])

            with st.expander("📚 Sources Used"):

                for i, (source, metadata) in enumerate(
                    zip(chat["sources"], chat["metadatas"]),
                    start=1
                ):
                    st.markdown(f"### 📄 {metadata['filename']}")
                    st.write(source)