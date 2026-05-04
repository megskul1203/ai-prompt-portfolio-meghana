\# Day 77 — Deployed RAG Pipeline to Public URL

\#\# What I understood today (in my own words)  
Streamlit Community Cloud reads your GitHub repo directly and builds  
your app in the cloud. The .env file stays local and secret — API keys  
go into Streamlit's Secrets manager instead, which works exactly the  
same way as dotenv but in the cloud.

\#\# What I actually tried  
\- Created requirements.txt so Streamlit Cloud knows what to install  
\- Created a Streamlit Community Cloud account via GitHub login  
\- Connected my GitHub repo to Streamlit Cloud  
\- Added GROQ\_API\_KEY safely in Advanced Settings → Secrets  
\- Deployed successfully — app is live at a public URL  
\- Tested live: grounded answers work, hallucination prevention works

\#\# One question I still have  
How do I share this effectively with recruiters on LinkedIn?  
