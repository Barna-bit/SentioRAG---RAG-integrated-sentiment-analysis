# 🧠 SentioRAG – RAG-Integrated Sentiment Analysis System

SentioRAG is a Retrieval-Augmented Generation (RAG) based sentiment analysis system that combines sentiment analysis, text processing, document retrieval, embeddings, and Generative AI to produce relevant and context-aware responses.

The system analyzes user input, identifies its sentiment, retrieves relevant information from the available knowledge base, and uses Google Gemini to generate a meaningful response based on the retrieved context.

---

## 🚀 Features

- 🔍 Sentiment analysis of user input
- 🧹 Text preprocessing and cleaning
- 📄 Document ingestion and processing
- 🧠 Text embedding generation
- 🔎 Semantic similarity-based document retrieval
- 📚 Retrieval-Augmented Generation (RAG)
- 🤖 Google Gemini integration for response generation
- 🌐 Flask-based web application
- 🔐 Secure API key management using environment variables
- 🗂️ FAISS-based vector storage and similarity search
- 🔗 LangChain-based RAG pipeline
- 🧩 Context-aware response generation using retrieved documents

---



Workflow Steps


1.User Input
The user enters a text query through the web interface.

2.Text Preprocessing
The input is cleaned and prepared for further processing.

3.Sentiment Analysis
The input text is analyzed to determine its sentiment.

4.Document Processing
Documents are loaded and processed to prepare them for retrieval.

5.Embedding Generation
Processed text is converted into vector embeddings.

6.Information Retrieval
Relevant documents are retrieved based on semantic similarity.

7.RAG Response Generation
The retrieved context and user input are passed to the generative AI model.

8.Final Response
Google Gemini generates a relevant and context-aware response.

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **LangChain**
- **Google Gemini API**
- **FAISS (Facebook AI Similarity Search)**
- **Sentence Transformers / Embeddings**
- **Natural Language Processing (NLP)**
- **HTML / CSS**
- **Git & GitHub**

📂 Project Structure

SentioRAG/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── src/
│   ├── app/
│   │   ├── templates/
│   │   │   └── index.html
│   │   ├── app.py
│   │   └── flask_app.py
│   │
│   ├── generation/
│   │   └── generate_response.py
│   │
│   ├── ingestion/
│   │   └── load_data.py
│   │
│   ├── processing/
│   │   ├── create_embeddings.py
│   │   └── preprocess.py
│   │
│   └── retrieval/
│       ├── langchain_rag.py
│       ├── retrieve.py
│       └── vector_store.py
│
├── .gitignore
├── README.md
└── requirements.txt


⚙️ Installation

1. Clone the Repository
git clone https://github.com/Barna-bit/SentioRAG---RAG-integrated-sentiment-analysis.git
2. Navigate to the Project
cd SentioRAG---RAG-integrated-sentiment-analysis
3. Create a Virtual Environment
python -m venv .venv
4. Activate the Virtual Environment
For Windows:
.venv\Scripts\activate
5. Install Dependencies
pip install -r requirements.txt


🔑 Environment Variables

Create a .env file in the project root directory.
GEMINI_API_KEY=your_api_key_here
Replace your_api_key_here with your own Google Gemini API key.
⚠️ Security Note: Never upload your actual API key or .env file to GitHub.
The .env file is excluded using .gitignore.


▶️ Running the Application

After activating the virtual environment and installing the dependencies, run:
python src/app/app.py
The Flask application will start locally.
Open the URL displayed in the terminal, usually:
http://127.0.0.1:5000/


💡 Use Cases

SentioRAG can be used for:
Customer feedback analysis
Review sentiment analysis
Context-aware question answering
Customer support applications
NLP-based information retrieval
AI-assisted feedback understanding


🔮 Future Improvements

Improve sentiment classification accuracy
Add support for multiple document formats
Implement conversation history
Add more advanced retrieval strategies
Deploy the application to a cloud platform
Add evaluation metrics for RAG responses
Improve the user interface

👩‍💻 Author
Barna-bit
GitHub:
https://github.com/Barna-bit⁠�

📜 License
This project is created for educational and development purposes.

## 🏗️ System Workflow

```text
User Input
    ↓
Text Preprocessing
    ↓
Sentiment Analysis
    ↓
Generate Embeddings
    ↓
FAISS Vector Store
    ↓
Similarity Search / Retrieval
    ↓
Relevant Context
    ↓
LangChain RAG Pipeline
    ↓
Google Gemini
    ↓
Context-Aware Response
