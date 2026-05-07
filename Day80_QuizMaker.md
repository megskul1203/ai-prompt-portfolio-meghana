\# Day 80 — AI Quiz Maker

\#\# What I understood today (in my own words)  
Asking the AI to return JSON instead of plain text is a game changer.  
When the output is structured data, I can parse it and display each  
question, option, and answer separately in the UI — instead of just  
printing a wall of text. The AI becomes a data generator, not just  
a text generator. This is how real AI products work under the hood.

\#\# What I actually tried  
\- Built an AI Quiz Maker that takes any training content as input  
\- Added controls for number of questions (3/5/8/10) and difficulty level  
\- Prompted the AI to return ONLY valid JSON — no explanation, no markdown  
\- Parsed the JSON and displayed each question with expandable answer reveals  
\- Added a download button so the quiz can be saved as a .txt file  
\- Tested with RAG and Embeddings content — 5 questions, all publication ready  
\- Deployed to Streamlit Community Cloud as third live app

\#\# One question I still have  
What if the AI returns badly formatted JSON and the parser breaks?  
(Answer: I already handled this — the try/except block catches JSON errors  
and shows the raw output instead of crashing the app)  
