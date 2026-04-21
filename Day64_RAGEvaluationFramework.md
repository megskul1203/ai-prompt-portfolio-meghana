#### **\*\*Day 64 \- RAG EVALUATION EVALUATION\*\***

\=== DAY 64: RAG EVALUATION FRAMEWORK \===

Current portfolio: ai-prompt-portfolio-meghana (63/90 skills)  
Day 63: RAG evaluation framework ✓  
Goal: Day 64/90 → Build a practical evaluation framework for RAG

GIVE ME:

1\. RAG evaluation framework structure  
2\. Metrics to track for retrieval \+ generation  
3\. One Freshworks support example  
4\. One table of metrics and what they mean  
5\. A short template for Day64\_RAGEvaluationFramework.md

\#\#\# Example query  
"Freshservice ticket timeout on Windows"

\#\#\# Output format  
\# Day 64: RAG Evaluation Framework

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

Day 64: RAG Evaluation Framework

Framework

👉 A simple practical structure to evaluate RAG:

* **Retrieval quality** → Did we get the right chunks?  
* **Context relevance** → Do those chunks match the query?  
* **Faithfulness** → Did the answer stick to the data?  
* **Answer usefulness** → Is the answer clear and helpful?

---

Freshworks example

🧾 Query:

“Freshservice ticket timeout on Windows”

---

🔎 Retrieved chunks:

* KB: “Windows timeout fix”  
* Chunk: “Increase timeout to 30 seconds”

---

🤖 Answer:

“Increase the timeout setting to 30 seconds in Windows to resolve the issue.”

---

✅ Evaluation:

* Retrieval quality → correct chunks  
* Context relevance → matches query  
* Faithfulness → no extra info added  
* Answer usefulness → clear fix provided

---

Metrics table

| Metric | What it checks |
| ----- | ----- |
| Precision | Are retrieved chunks relevant and useful? |
| Recall | Did we retrieve all important information? |
| Relevance | How closely chunks match the query |
| Faithfulness | Is the answer based only on retrieved data? |
| Hallucination rate | How often the model makes up information |
| Answer usefulness | Is the answer clear and actionable |

---

📄 Template: Day64\_RAGEvaluationFramework.md

\# Day 64: RAG Evaluation Framework

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
\- Precision: High  
\- Recall: Good  
\- Faithfulness: High  
\- Hallucination: None  
\- Usefulness: Clear and helpful

\#\# Key Idea  
Good RAG \= right data \+ correct answer

---

💡 Key idea

Good RAG works only when both retrieval and answer are correct.

