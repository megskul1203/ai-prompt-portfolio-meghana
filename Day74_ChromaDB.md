\#\# Day 74: ChromaDB — Vector Database

\#\#\# What I understood today (in my own words)  
ChromaDB is a database designed specifically for storing embeddings.   
Unlike a regular database that stores text and searches by exact keywords,   
ChromaDB stores vectors and searches by meaning similarity. A collection   
is like a table — it stores documents, their embeddings, and unique IDs   
together. The hnsw:space cosine setting tells ChromaDB to measure   
similarity using cosine similarity — without this it uses a different   
metric that gives wrong results (negative scores). The key advantage over   
Day 73's approach: ChromaDB handles all searching internally and would   
work just as fast with 1 million documents.

\#\#\# What I actually tried  
Built a ChromaDB knowledge base with 12 AI concepts from my 73-day   
portfolio. Added documents \+ embeddings \+ IDs in one operation. Ran 4   
semantic searches — all returned correct, relevant results with positive   
similarity scores (0.3–0.6 range). 

Key discovery: had to explicitly set cosine similarity metric — default   
metric gave negative scores. Debugging this taught me that database   
configuration matters as much as the code itself.

\#\#\# One question I still have  
Right now the database resets every time the script runs — it's   
in-memory only. How do I make it persist permanently so I don't   
rebuild it every time?  
(Answer: chromadb.PersistentClient() — tomorrow's RAG pipeline will use this)  
