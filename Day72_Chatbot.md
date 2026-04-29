\#\# Day 72: Chatbot with Memory

\#\#\# What I understood today (in my own words)  
AI APIs have zero memory by default — every call starts fresh. Memory   
is created by sending the entire conversation history in the messages   
list every single time. The list grows with each exchange: system prompt   
\+ user message \+ AI reply \+ next user message \+ next AI reply... and so   
on. A while True loop runs forever until a condition breaks it — in this   
case typing "quit". The system prompt is the personality and instructions   
for the AI — writing it is exactly what prompt engineers do professionally.

\#\#\# What I actually tried  
Built a personal AI tutor chatbot with:  
\- A custom system prompt making it an L\&D-aware AI tutor for Meghana  
\- Full conversation memory — tested across 3 questions, memory grew   
  from 3 to 7 messages  
\- while True loop with quit condition and empty input handling  
\- Memory counter showing the growing conversation history in real time

Tested: asked about RAG, then L\&D connection, then corporate training   
example. Each answer correctly built on the previous — memory confirmed working.

\#\#\# One question I still have  
What happens when the conversation gets very long — does sending   
thousands of messages slow down or break the API?   
(Answer: yes — this is why production chatbots use summarisation   
or sliding window memory. Day 20 of my portfolio covered this\!)  
