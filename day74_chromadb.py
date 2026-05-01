import chromadb
from sentence_transformers import SentenceTransformer

# Load the same embedding model from Day 73
print("Loading embedding model...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("Model loaded!\n")

# Create a ChromaDB client — stores data in memory for now
client = chromadb.Client()

# Create a collection — like a table in a database
collection = client.create_collection(
    name="ai_knowledge_base",
    metadata={"hnsw:space": "cosine"}
)

# Your knowledge base — AI concepts you've studied for 73 days
documents = [
    "RAG stands for Retrieval Augmented Generation. It retrieves relevant documents before generating answers to reduce hallucinations.",
    "Vector search finds the most semantically similar text using embedding vectors and cosine similarity.",
    "Fine-tuning updates a model's weights on new training data to specialise its behaviour for specific tasks.",
    "Chain of thought prompting asks the model to reason step by step before giving a final answer.",
    "Hallucination happens when an LLM confidently states something that is factually incorrect.",
    "ChromaDB is a vector database that stores embeddings and enables fast similarity search at scale.",
    "Embeddings convert text into lists of numbers called vectors — similar meanings produce similar vectors.",
    "A system prompt defines the personality and rules for an AI assistant across all conversations.",
    "RAGAS evaluates RAG pipelines using metrics like faithfulness, answer relevancy, and context precision.",
    "Agentic RAG uses AI agents that can decide which tools to use and how to retrieve information dynamically.",
    "L&D professionals design learning experiences to improve knowledge, skills, and performance at work.",
    "Prompt engineering is the practice of designing precise instructions to get reliable outputs from LLMs."
]

# Create IDs for each document
ids = [f"doc{i}" for i in range(len(documents))]

# Generate embeddings for all documents
print("Generating embeddings for knowledge base...")
embeddings = model.encode(documents).tolist()

# Add everything to ChromaDB
collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=ids
)
print(f"Added {len(documents)} documents to ChromaDB\n")

# Search function
def search(query, top_k=3):
    print(f"Query: '{query}'")
    print("-" * 60)
    
    # Convert query to embedding
    query_embedding = model.encode([query]).tolist()[0]
    
    # Search ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    
    # Print results
    for i, (doc, distance) in enumerate(zip(
        results['documents'][0],
        results['distances'][0]
    )):
        similarity = 1 - distance
        print(f"{i+1}. Similarity {similarity:.3f}: {doc}")
    print()

# Run searches
search("How does RAG prevent AI from making things up?")
search("What tools help evaluate AI pipeline quality?")
search("How do I design better learning experiences using AI?")
search("What is the difference between RAG and fine-tuning?")