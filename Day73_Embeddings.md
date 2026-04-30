\#\# Day 73: Embeddings — Text as Numbers

\#\#\# What I understood today (in my own words)  
Embeddings convert text into lists of numbers called vectors — each   
sentence becomes 384 numbers. Similar meanings produce similar numbers.   
Cosine similarity measures how close two vectors are — score near 1 means   
very similar, near 0 means completely different. This is how semantic   
search works — finding relevant content by meaning, not just matching   
exact words. This is the R in RAG — Retrieval. Find the most similar   
chunks to the user's question, pass them to the LLM, get a grounded answer.

\#\#\# What I actually tried  
Built a semantic search engine using sentence-transformers (free, local,   
no API needed). Converted 7 sentences into embeddings, then searched with   
3 queries. Key results:  
\- "How does RAG prevent making up facts?" → correctly found RAG \+   
  hallucination sentences without using those exact words  
\- "How to teach step by step?" → found Chain of Thought AND L\&D   
  sentences — connected teaching to L\&D by meaning alone  
\- "Improve training content for learners?" → L\&D sentence scored 0.452,   
  highest match — perfect

The model found relevant results purely by meaning — never matched exact   
words. That is semantic search working in real code.

\#\#\# One question I still have  
How do I store these embeddings permanently so I don't have to   
recalculate them every time the script runs?   
(Answer: this is exactly what ChromaDB does — Day 74 tomorrow\!)  
