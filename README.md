# 📄 AI Document Assistant (RAG)

A Retrieval-Augmented Generation (RAG) application that enables users to upload documents and ask questions using a local Large Language Model (Llama 3.2). The application retrieves relevant document chunks using semantic search and generates accurate answers based on the uploaded content.

---

## 🚀 Features

- 📂 Upload multiple documents
- 📄 Supports PDF, DOCX, PPTX, and TXT files
- 🤖 Question Answering using Llama 3.2 (Ollama)
- 🔍 Semantic Search using Sentence Transformers
- 🗂 Vector Database with ChromaDB
- 💬 Chat-style interface using Streamlit
- 📚 Displays source chunks used to answer questions
- 🏷 Metadata support (filename displayed with retrieved sources)
- 🗑 Clear Chat functionality

---

## 🛠 Tech Stack

- Python
- Streamlit
- Ollama
- Llama 3.2
- ChromaDB
- Sentence Transformers
- LangChain Text Splitters
- PyPDF
- python-docx
- python-pptx

---

## 📂 Project Structure

```
AI-Document-Assistant-RAG/
│
├── app.py
├── rag.py
├── vector_db.py
├── embeddings.py
├── document_loader.py
├── utils.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── documents/
├── data/
```

---

## ⚙ Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Document-Assistant-RAG.git
cd AI-Document-Assistant-RAG
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download Ollama from:

https://ollama.com/download

Pull the model:

```bash
ollama pull llama3.2
```

---

## ▶ Run the Application

```bash
streamlit run app.py
```

---

## 📖 How to Use

1. Launch the Streamlit application.
2. Upload one or more documents (PDF, DOCX, PPTX, or TXT).
3. Wait for the documents to be processed.
4. Enter a question in the chat box.
5. View the generated answer along with the retrieved source chunks.

---

## 📸 Screenshots

Add screenshots of:

- Home Page
- Document Upload
- Question Answering
- Source Display

---

## 🔮 Future Improvements

- Page-level metadata
- Citation highlighting
- Drag-and-drop upload
- Persistent vector database
- Conversation memory
- Support for additional document formats

---

## 👨‍💻 Author

**Kusuma Reddy**

GitHub: https://github.com/siripikusumareddy

---

## 📄 License

This project is licensed under the MIT License.
