\#\# Day 70: Prompt Templates \+ Loops

\#\#\# What I understood today (in my own words)  
A function is a reusable block of code — write once, use many times.  
An f-string lets you drop variables into text using {} so one template  
generates many different prompts. A for loop automatically repeats an  
action for every item in a list — I used it to send 5 different prompts  
to the AI in one run without writing 5 separate calls.

\#\#\# What I actually tried  
Built a prompt template function that takes topic \+ audience as inputs  
and generates a customised AI explanation. Ran it across 5 different  
topic/audience combinations in one loop. Discovered that "RAG" gave  
wrong results until I wrote "RAG (Retrieval Augmented Generation)" —  
proved that prompt specificity directly changes output quality.

