# 🚀 RAG-based AI System (Modular & Production-Ready)

A **modular Retrieval-Augmented Generation (RAG) system** designed with an industry-standard architecture for scalability, maintainability, and real-world deployment.

---

## 📌 Project Overview

This project transforms a **Jupyter Notebook-based RAG pipeline** into a **clean, modular Python system**.

It supports:

* 📄 Data ingestion (PDF/Text)
* ✂️ Text chunking
* 🧠 Embedding generation (Sentence Transformers)
* 🗄️ Vector storage (ChromaDB)
* 🔍 Semantic retrieval
* 🤖 LLM response generation (Groq)

---

## 🧠 Architecture

```text
Data → Chunking → Embedding → Vector DB → Retrieval → LLM → Response
```

---

## 📂 Project Structure

```text
src/
├── config/           # Configuration settings
├── data_ingestion/   # Load PDF/Text data
├── data_chunk/       # Text chunking logic
├── data_embedding/   # Embedding generation
├── vector_store/     # ChromaDB integration
├── retrival/         # Retrieval logic (RAG)
├── llm_output/       # LLM interaction
├── pipeline/         # Query pipeline orchestration
├── utils/            # Logger & helpers
```

---

## ⚙️ Tech Stack

* **LangChain** (core framework)
* **ChromaDB** (vector database)
* **Sentence Transformers** (embeddings)
* **FAISS** (similarity backend support)
* **Groq API** (LLM inference)
* **PyMuPDF / PyPDF** (document processing)
* **python-dotenv** (environment management)
* **Typesense** (optional search support)

---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/devendraaa/Rag-project-1.git
cd Rag-project-1
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 🧪 Example Query

```text
What is layer normalization?
```

---

## 📊 Logging

* Logs are generated for each run:

```text
logs/app_<timestamp>.log
```

Includes:

* Pipeline execution steps
* Embedding process
* Retrieval activity
* Query execution time

---

## ⚡ Features

* ✅ Modular architecture (industry standard)
* ✅ Clean separation of components
* ✅ Persistent vector database
* ✅ Incremental data ingestion support
* ✅ Logging system (file + console)
* ✅ Environment-based configuration
* ✅ Ready for API integration (FastAPI)

---

## 🧠 Key Concepts

* Retrieval-Augmented Generation (RAG)
* Vector similarity search
* Cosine similarity
* Embedding-based retrieval
* Modular AI system design

---

## 🚀 Future Improvements

* 🔥 FastAPI backend integration
* 🔥 Streamlit UI
* 🔥 Docker deployment
* 🔥 Multi-user query handling
* 🔥 Agent-based workflows (LangGraph)

---

## 🔐 Security

* API keys stored in `.env`
* `.env` excluded via `.gitignore`
* No secrets stored in repository

---

## 👨‍💻 Author

**Devendra Umesh Chavan**
AI Engineer | Founder

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
