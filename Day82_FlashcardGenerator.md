\# Day 82 — AI Flashcard Generator

\#\# What I understood today (in my own words)  
Flashcards work through active recall — forcing the brain to retrieve  
information rather than just recognise it. The prompt had to encode this  
instructional design principle explicitly — "promote active recall, not  
just recognition." The AI didn't know good flashcard design until I told  
it. My L\&D knowledge made the output better than a generic prompt would.

\#\# What I actually tried  
\- Built a Streamlit app that generates flashcards from any training content  
\- Used JSON output so each card displays separately as an expandable widget  
\- Added difficulty levels that change the type of questions generated  
\- Beginner \= definitions, Intermediate \= how/why, Advanced \= application  
\- Tested with RAG content — 8 intermediate cards, all active recall quality  
\- Deployed as fifth live app on Streamlit Community Cloud

\#\# One question I still have  
Could I combine the Quiz Maker and Flashcard Generator into one  
L\&D toolkit app with multiple tabs?  
