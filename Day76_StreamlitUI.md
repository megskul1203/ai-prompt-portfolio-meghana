\# Day 76 — Streamlit UI for RAG Pipeline

\#\# What I understood today (in my own words)  
Streamlit turns a Python script into a real web app with just a few extra lines.  
@st.cache\_resource is like a "don't reload this expensive thing" decorator — it keeps  
ChromaDB and the embedding model in memory between questions so the app doesn't  
reload them on every single query.  
The RAG logic is 100% identical to Day 75 — Streamlit just gives it a face that  
anyone can use in a browser.

\#\# What I actually tried  
\- Installed Streamlit using pip  
\- Wrapped the complete Day 75 RAG pipeline in a Streamlit UI  
\- Added a text input box, Ask button, answer display, and sources section  
\- Used @st.cache\_resource to avoid reloading models on every question  
\- Ran it locally at localhost:8501  
\- Tested 3 questions:  
  \- "What is RAG?" → perfect grounded answer from correct documents ✅  
  \- "How does Freshworks use RAG?" → found Freddy AI document specifically ✅  
  \- "What is the capital of France?" → correctly refused to hallucinate ✅

\#\# One question I still have  
How do I deploy this to a public URL so recruiters can actually click it?  
(Answer: Streamlit Community Cloud — that's Day 77\!)  
