from sentence_transformers import SentenceTransformer
import numpy as np

# Load a free embedding model — runs on your computer, no API needed
print("Loading embedding model...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("Model loaded!\n")

# These are your knowledge base chunks — like a mini RAG database
sentences = [
    "RAG retrieves documents before generating answers to reduce hallucinations",
    "Vector search finds similar text using mathematical embeddings",
    "Fine-tuning updates a model's weights on new data to specialise its behaviour",
    "Chain of thought prompting asks the model to reason step by step",
    "Hallucination happens when an LLM confidently states something factually incorrect",
    "L&D professionals design learning experiences to improve knowledge and performance",
    "Embeddings convert text into numbers so computers can measure meaning similarity"
]

# Convert all sentences to embeddings (vectors/numbers)
print("Converting sentences to embeddings...")
embeddings = model.encode(sentences)
print(f"Each sentence is now {len(embeddings[0])} numbers\n")

# Cosine similarity function — measures how similar two vectors are
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot_product / (norm1 * norm2)

# Search function — finds most similar sentences to a query
def search(query, top_k=3):
    print(f"Query: '{query}'")
    print("-" * 50)
    
    # Convert query to embedding
    query_embedding = model.encode([query])[0]
    
    # Compare query to every sentence
    scores = []
    for i, sentence in enumerate(sentences):
        score = cosine_similarity(query_embedding, embeddings[i])
        scores.append((score, sentence))
    
    # Sort by highest similarity score
    scores.sort(reverse=True)
    
    # Show top results
    for i, (score, sentence) in enumerate(scores[:top_k]):
        print(f"{i+1}. Score {score:.3f}: {sentence}")
    print()

# Run 3 different searches
search("How does RAG prevent AI from making up facts?")
search("What is the best way to teach someone step by step?")
search("How do I improve my training content for learners?")