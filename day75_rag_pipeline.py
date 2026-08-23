import chromadb
from sentence_transformers import SentenceTransformer
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

# ── Step 1: Load models ──────────────────────────────────────────
print("Loading models...")
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
print("Models loaded!\n")

# ── Step 2: Build knowledge base in ChromaDB ─────────────────────
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(
    name="rag_knowledge_base",
    metadata={"hnsw:space": "cosine"}
)

knowledge_base = [
    "RAG stands for Retrieval Augmented Generation. It retrieves relevant documents before generating answers to reduce hallucinations.",
    "Vector search finds the most semantically similar text using embedding vectors and cosine similarity scores.",
    "Fine-tuning updates a model's weights on new training data to specialise its behaviour for a specific domain.",
    "Chain of thought prompting asks the model to reason step by step before giving a final answer.",
    "Hallucination in AI happens when an LLM confidently states something that is factually incorrect or made up.",
    "ChromaDB is a vector database that stores embeddings and enables fast similarity search at scale.",
    "Embeddings convert text into lists of numbers called vectors — similar meanings produce similar vectors.",
    "A system prompt defines the personality, rules, and context for an AI assistant across all conversations.",
    "RAGAS evaluates RAG pipelines using metrics like faithfulness, answer relevancy, and context precision.",
    "Agentic RAG uses AI agents that can decide which tools to use and retrieve information dynamically.",
    "L&D professionals design learning experiences to improve knowledge, skills, and performance at work.",
    "Prompt engineering is designing precise instructions to get reliable and accurate outputs from LLMs.",
    "Cosine similarity measures the angle between two vectors — score near 1 means very similar meaning.",
    "A knowledge base is a collection of documents that a RAG system retrieves answers from.",
    "Context window is the maximum amount of text an LLM can process in a single call.",
    "Chunking is splitting large documents into smaller pieces so they fit in the context window.",
    "Freshworks Freddy AI uses RAG to answer customer queries using help desk articles as knowledge base.",
    "Sarvam AI is a Bengaluru startup building AI models for Indian languages and enterprise use cases.",
    "Instructional design is the process of creating effective learning experiences using systematic approaches.",
    "An LLM is a Large Language Model trained on massive text data to understand and generate human language."
]

ids = [f"doc{i}" for i in range(len(knowledge_base))]

print("Building knowledge base...")
embeddings = embedding_model.encode(knowledge_base).tolist()
collection.add(
    documents=knowledge_base,
    embeddings=embeddings,
    ids=ids
)
print(f"Knowledge base ready — {len(knowledge_base)} documents stored\n")

# ── Step 3: The RAG function ─────────────────────────────────────
def rag_answer(question, top_k=3):
    # RETRIEVE — find relevant documents
    query_embedding = embedding_model.encode([question]).tolist()[0]
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    retrieved_docs = results['documents'][0]

    # BUILD CONTEXT — combine retrieved docs
    context = "\n\n".join([f"- {doc}" for doc in retrieved_docs])

    # AUGMENT — create grounded prompt
    prompt = f"""You are a helpful AI assistant. Answer the question using 
ONLY the context provided below. If the answer is not in the context, 
say "I don't have enough information to answer that."

Context:
{context}

Question: {question}

Answer:"""

    # GENERATE — call Groq with context
    response = groq_client.chat.completions.create(
    model="openai/gpt-oss-120b",   # was "llama-3.3-70b-versatile"
    messages=[{"role": "user", "content": prompt}]
)
    

    answer = response.choices[0].message.content
    return answer, retrieved_docs

# ── Step 4: Run the RAG pipeline ────────────────────────────────
questions = [
    "What is RAG and how does it reduce hallucinations?",
    "How does Freshworks use RAG in their product?",
    "What metrics should I use to evaluate my RAG pipeline?",
    "How does my L&D background help in AI engineering?",
    "What is the difference between RAG and fine-tuning?"
]

print("=" * 60)
print("RAG PIPELINE — Day 75")
print("=" * 60)

for question in questions:
    print(f"\nQ: {question}")
    print("-" * 60)
    answer, sources = rag_answer(question)
    print(f"A: {answer}")
    print(f"\nSources used:")
    for source in sources:
        print(f"  → {source[:80]}...")
    print()