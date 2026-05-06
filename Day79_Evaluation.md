\# Day 79 — RAG Pipeline Evaluation

\#\# What I understood today (in my own words)  
Evaluation turns "my pipeline works" into "my pipeline scores 0.88 faithfulness."  
RAGAS couldn't install on Python 3.14 so I built my own evaluator using the  
Groq API itself as the judge — this is called LLM-as-a-judge evaluation,  
which is actually a widely used technique in the industry.  
The scores revealed something important: low scores don't always mean failure.  
Question 4 (capital of France) scored 0.00 on relevancy and precision — but  
that's correct behaviour. The pipeline was honest about not knowing.

\#\# What I actually tried  
\- Tried installing RAGAS — failed due to Python 3.14 incompatibility  
\- Built a custom evaluator measuring three metrics:  
  \- Faithfulness: is the answer grounded in retrieved context?  
  \- Answer Relevancy: does the answer address the question?  
  \- Context Precision: did ChromaDB retrieve the right documents?  
\- Ran evaluation on 4 test questions  
\- Results:  
  \- "What is RAG?" → 1.00 / 1.00 / 1.00 (perfect)  
  \- "How does Freshworks use RAG?" → 1.00 / 0.80 / 0.80 (good)  
  \- "RAG evaluation metrics?" → 0.50 / 0.00 / 0.80 (needs more docs)  
  \- "Capital of France?" → 1.00 / 0.00 / 0.00 (correctly refused)  
\- Overall pipeline score: 0.66 (0.82 excluding out-of-scope question)

\#\# One question I still have  
How do I improve the score for Question 3?  
(Answer: add more documents about RAGAS metrics to the knowledge base)

