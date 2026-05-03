import streamlit as st
import chromadb
from chromadb.utils import embedding_functions
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

# ── Page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="Meghana's RAG Assistant",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Meghana's RAG Pipeline")
st.markdown("Ask anything about **AI, RAG, embeddings, or L&D**. Answers are grounded in a real knowledge base — no hallucination.")

# ── Load models (cached so they don't reload on every question) ──
@st.cache_resource
def load_resources():
    ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    client = chromadb.Client()
    collection = client.get_or_create_collection(
        name="rag_knowledge_base",
        metadata={"hnsw:space": "cosine"}
    )

    # Knowledge base — same 20 docs from Day 75
    documents = [
        "RAG stands for Retrieval Augmented Generation. It combines a retrieval system with a language model.",
        "In RAG, the retrieval step finds relevant documents from a knowledge base using semantic search.",
        "The augmentation step in RAG injects retrieved documents into the prompt as context for the LLM.",
        "The generation step in RAG uses the LLM to produce an answer grounded in retrieved context.",
        "RAG prevents hallucination by instructing the model to answer only from provided context.",
        "Embeddings are numerical representations of text, typically vectors of 384 or 768 dimensions.",
        "Cosine similarity measures the angle between two vectors. Score of 1.0 means identical meaning.",
        "ChromaDB is a vector database that stores embeddings and enables fast semantic search.",
        "Sentence-transformers is a Python library that converts text to embeddings locally without an API.",
        "The all-MiniLM-L6-v2 model creates 384-dimensional embeddings and runs on CPU for free.",
        "RAGAS is a framework for evaluating RAG pipelines using metrics like faithfulness and relevancy.",
        "Faithfulness in RAGAS measures whether the answer is grounded in the retrieved context.",
        "Answer relevancy in RAGAS measures how well the answer addresses the original question.",
        "Context precision in RAGAS measures whether retrieved chunks are actually relevant to the query.",
        "Freshworks Freddy AI uses RAG to answer customer support questions from help center documents.",
        "Freddy AI retrieves relevant help articles before generating responses to avoid hallucination.",
        "Prompt engineering is the practice of designing inputs to get better outputs from language models.",
        "L&D stands for Learning and Development — the field focused on training and education in organizations.",
        "Instructional design involves creating structured learning experiences with clear objectives and assessments.",
        "LLMs are Large Language Models trained on vast text data to understand and generate human language.",
    ]

    ids = [f"doc_{i}" for i in range(len(documents))]
    embeddings = ef(documents)

    # Only add if collection is empty (avoids duplicate errors on rerun)
    if collection.count() == 0:
        collection.add(documents=documents, embeddings=embeddings, ids=ids)

    groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    return collection, ef, groq_client

collection, ef, groq_client = load_resources()

# ── RAG function ──────────────────────────────────────────────
def rag_answer(question):
    # RETRIEVE
    query_embedding = ef([question])
    results = collection.query(query_embeddings=query_embedding, n_results=3)
    retrieved_docs = results["documents"][0]

    # AUGMENT
    context = "\n".join([f"- {doc}" for doc in retrieved_docs])
    prompt = f"""You are a helpful AI assistant. Answer the question using ONLY the context below.
If the context does not contain enough information, say "I don't have enough information in my knowledge base to answer this."

Context:
{context}

Question: {question}
Answer:"""

    # GENERATE
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    answer = response.choices[0].message.content
    return answer, retrieved_docs

# ── UI ────────────────────────────────────────────────────────
question = st.text_input("💬 Ask your question:", placeholder="e.g. What is RAG? How does Freshworks use RAG?")

if st.button("Ask") and question.strip():
    with st.spinner("Searching knowledge base and generating answer..."):
        answer, sources = rag_answer(question)

    st.markdown("### 💡 Answer")
    st.write(answer)

    st.markdown("### 📚 Sources Retrieved")
    for i, doc in enumerate(sources, 1):
        st.markdown(f"**{i}.** {doc}")

st.markdown("---")
st.caption("Built by Meghana · Day 76 · RAG Pipeline with Streamlit")