from groq import Groq
from dotenv import load_dotenv
import chromadb
from chromadb.utils import embedding_functions
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# ── Rebuild knowledge base ────────────────────────────────────
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(
    name="eval_knowledge_base",
    metadata={"hnsw:space": "cosine"}
)

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
    "Faithfulness measures whether the answer is grounded in the retrieved context.",
    "Answer relevancy measures how well the answer addresses the original question.",
    "Context precision measures whether retrieved chunks are actually relevant to the query.",
    "Freshworks Freddy AI uses RAG to answer customer support questions from help center documents.",
    "Freddy AI retrieves relevant help articles before generating responses to avoid hallucination.",
    "Prompt engineering is the practice of designing inputs to get better outputs from language models.",
    "L&D stands for Learning and Development — the field focused on training and education in organizations.",
    "Instructional design involves creating structured learning experiences with clear objectives.",
    "LLMs are Large Language Models trained on vast text data to understand and generate human language.",
]

ids = [f"doc_{i}" for i in range(len(documents))]
embeddings = ef(documents)
collection.add(documents=documents, embeddings=embeddings, ids=ids)

# ── RAG function ──────────────────────────────────────────────
def rag_answer(question):
    query_embedding = ef([question])
    results = collection.query(query_embeddings=query_embedding, n_results=3)
    retrieved_docs = results["documents"][0]
    context = "\n".join([f"- {doc}" for doc in retrieved_docs])
    prompt = f"""Answer using ONLY the context below. If context is insufficient, 
say "I don't have enough information."

Context:
{context}

Question: {question}
Answer:"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content, retrieved_docs

# ── Evaluation functions ──────────────────────────────────────
def evaluate_faithfulness(question, answer, context_docs):
    context = "\n".join([f"- {doc}" for doc in context_docs])
    prompt = f"""You are an evaluator. Given a question, an answer, and the context 
documents used to generate the answer, rate the FAITHFULNESS of the answer.

Faithfulness means: Is every claim in the answer supported by the context? 
Does the answer avoid adding information not present in the context?

Question: {question}
Answer: {answer}
Context: {context}

Rate faithfulness from 0.0 to 1.0 where:
1.0 = every claim is fully supported by context
0.5 = some claims supported, some not
0.0 = answer ignores or contradicts context

Reply with ONLY a number between 0.0 and 1.0. Nothing else."""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return float(response.choices[0].message.content.strip())

def evaluate_answer_relevancy(question, answer):
    prompt = f"""You are an evaluator. Rate how well the answer addresses the question.

Question: {question}
Answer: {answer}

Rate answer relevancy from 0.0 to 1.0 where:
1.0 = answer directly and completely addresses the question
0.5 = answer partially addresses the question
0.0 = answer is off-topic or does not address the question

Reply with ONLY a number between 0.0 and 1.0. Nothing else."""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return float(response.choices[0].message.content.strip())

def evaluate_context_precision(question, context_docs):
    context = "\n".join([f"- {doc}" for doc in context_docs])
    prompt = f"""You are an evaluator. Rate how relevant the retrieved context 
documents are to the question.

Question: {question}
Retrieved Context: {context}

Rate context precision from 0.0 to 1.0 where:
1.0 = all retrieved documents are highly relevant to the question
0.5 = some documents relevant, some not
0.0 = retrieved documents are completely irrelevant

Reply with ONLY a number between 0.0 and 1.0. Nothing else."""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return float(response.choices[0].message.content.strip())

# ── Test questions ────────────────────────────────────────────
test_questions = [
    "What is RAG?",
    "How does Freshworks use RAG?",
    "What are RAG evaluation metrics?",
    "What is the capital of France?",
]

# ── Run evaluation ────────────────────────────────────────────
print("=" * 60)
print("RAG PIPELINE EVALUATION REPORT")
print("=" * 60)

total_faithfulness = 0
total_relevancy = 0
total_precision = 0
count = 0

for question in test_questions:
    print(f"\nQuestion: {question}")
    print("-" * 40)

    answer, context_docs = rag_answer(question)
    print(f"Answer: {answer[:150]}...")

    faithfulness = evaluate_faithfulness(question, answer, context_docs)
    relevancy = evaluate_answer_relevancy(question, answer)
    precision = evaluate_context_precision(question, context_docs)

    print(f"Faithfulness:      {faithfulness:.2f}")
    print(f"Answer Relevancy:  {relevancy:.2f}")
    print(f"Context Precision: {precision:.2f}")

    total_faithfulness += faithfulness
    total_relevancy += relevancy
    total_precision += precision
    count += 1

print("\n" + "=" * 60)
print("OVERALL SCORES")
print("=" * 60)
print(f"Average Faithfulness:      {total_faithfulness/count:.2f}")
print(f"Average Answer Relevancy:  {total_relevancy/count:.2f}")
print(f"Average Context Precision: {total_precision/count:.2f}")
print(f"Overall Pipeline Score:    {(total_faithfulness + total_relevancy + total_precision)/(count*3):.2f}")
print("=" * 60)