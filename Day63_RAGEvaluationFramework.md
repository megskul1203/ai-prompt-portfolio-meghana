#### **\*\*Day 63 \- RAG EVALUATION EVALUATION\*\***

\=== DAY 63: RAG EVALUATION FRAMEWORK \===

Current portfolio: ai-prompt-portfolio-meghana (62/90 skills)  
Day 62: Hallucination \+ faithfulness ✓  
Goal: Day 63/90 → Build a practical evaluation framework for RAG

GIVE ME:

1\. RAG evaluation framework structure  
2\. Metrics to track for retrieval \+ generation  
3\. One Freshworks support example  
4\. One table of metrics and what they mean  
5\. A short template for Day63\_RAGEvaluationFramework.md

\#\#\# Example query  
"Freshservice ticket timeout on Windows"

\#\#\# Output format  
\# Day 63: RAG Evaluation Framework

\#\# Framework  
\- Retrieval quality  
\- Context relevance  
\- Faithfulness  
\- Answer usefulness

\#\# Freshworks example  
\[one short example\]

\#\# Metrics table  
| Metric | What it checks |  
|---|---|  
| Precision | ... |  
| Recall | ... |  
| Faithfulness | ... |  
| Hallucination rate | ... |

\#\# Key idea  
\[one line only\]

**RESPONSE:**

Day 63: RAG Evaluation Framework  
---

Framework

👉 A simple way to evaluate RAG systems:

1️⃣ Retrieval Quality

* Did we fetch the **right chunks**?

2️⃣ Context Relevance

* Are the retrieved chunks **closely related to the query**?

3️⃣ Faithfulness

* Did the answer **stick to the retrieved data**?

4️⃣ Answer Usefulness

* Is the answer **clear, correct, and helpful to the user**?

Freshworks example

🧾 Query:

“Freshservice ticket timeout on Windows”

🔎 Retrieval

* KB: “Windows timeout fix”  
* Chunk: “Increase timeout to 30 seconds”

👉 Good retrieval ✅

🤖 Answer

“Increase the timeout setting to 30 seconds in Windows to fix the issue.”

👉 Evaluation:

* Retrieval Quality → ✅ correct chunks  
* Context Relevance → ✅ matches query  
* Faithfulness → ✅ no extra info  
* Usefulness → ✅ clear solution

Metrics table

| Metric | What it checks |
| ----- | ----- |
| Precision | Are retrieved chunks useful? |
| Recall | Did we miss important info? |
| Relevance | Do chunks match the query? |
| Faithfulness | Is answer based on retrieved data? |
| Hallucination rate | How often model makes up info |
| Answer usefulness | Is the answer helpful and clear |

📄 Template: Day63\_RAGEvaluationFramework.md

\# Day 63: RAG Evaluation Framework

\#\# Framework  
\- Retrieval quality  
\- Context relevance  
\- Faithfulness  
\- Answer usefulness

\#\# Example  
Query: "Freshservice ticket timeout on Windows"

Retrieved:  
\- KB: Windows timeout fix  
\- Chunk: Increase timeout to 30 seconds

Answer:  
"Increasing timeout to 30 seconds resolves the issue."

\#\# Evaluation  
\- Precision: High (relevant chunks)  
\- Recall: Good (no important info missed)  
\- Faithfulness: High (no hallucination)  
\- Usefulness: Clear and actionable

\#\# Key Idea  
Good RAG \= correct retrieval \+ faithful \+ useful answer

💡 Key idea

Good RAG \= right data retrieved \+ answer stays true and useful.

