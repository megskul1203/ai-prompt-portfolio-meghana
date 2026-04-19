#### **\*\*Day 62 \- HALLUCINATIONS\*\***

**\=== DAY 62: HALLUCINATION \+ FAITHFULNESS \===**

Current portfolio: ai-prompt-portfolio-meghana (61/90 skills)  
Day 61: Basic RAG evaluation metrics ✓ understood simply  
Goal: Day 62/90 → Understand hallucination and faithfulness clearly

I am still learning, so explain in very simple language:  
\- What hallucination means  
\- What faithfulness means  
\- Why a model can sound confident and still be wrong  
\- How RAG helps reduce hallucination  
\- Why retrieval alone is not enough

Please do NOT jump to advanced topics.  
Use:  
1\. Beginner-friendly explanation  
2\. One Freshworks support example  
3\. One comparison table  
4\. One short summary sentence

\#\#\# Example query  
"Freshservice ticket timeout on Windows"

Explain:  
\- what a hallucinated answer looks like  
\- what a faithful answer looks like  
\- how retrieved context keeps the answer grounded

\#\#\# Output format  
\# Day 62: Hallucination \+ Faithfulness

**RESPONSE:**

Simple explanation

🔹 What is hallucination

👉 Hallucination \= **the model gives an answer that sounds correct but is actually wrong**

* It may sound confident  
* It may look detailed  
* But it is **not based on real data**

---

🔹 What is faithfulness

👉 Faithfulness \= **the answer is fully based on the retrieved data**

* No extra guessing  
* No made-up steps  
* Only what is supported by context

---

🔹 Why a model can sound confident and still be wrong

Because LLMs are trained to:

Predict the most likely sentence → not verify truth

👉 So they can:

* Sound fluent ✅  
* Sound confident ✅  
* Still be wrong ❌

---

🔹 How RAG helps reduce hallucination  
RAG \= Retrieve real data → give to LLM → generate answer

👉 Now the model:

* Uses real KB articles  
* Uses real tickets  
* Is less likely to guess

---

🔹 Why retrieval alone is NOT enough

Even if retrieval is correct:

Good data → but model adds extra info → still wrong

👉 So we must check:

* Is answer using data? (faithfulness)  
* Is it adding new info? (hallucination)

---

Freshworks example

🧾 Query:

“Freshservice ticket timeout on Windows”

---

🔎 Retrieved context (correct)

* KB: “Windows timeout fix”  
* Chunk: “Increase timeout to 30 seconds”

---

❌ Hallucinated answer

“Restart the Linux server and reinstall network drivers.”

Why this is wrong:

* Not from retrieved data  
* Mentions Linux (irrelevant)  
* Completely made up

---

✅ Faithful answer

“Increase the timeout setting to 30 seconds in Windows to resolve the issue.”

Why this is correct:

* Matches retrieved chunk  
* No extra information  
* Fully grounded in data

---

🔗 How context keeps answer grounded  
Retrieve correct chunk  
→ Give to LLM  
→ LLM uses only that info  
→ Answer stays accurate

---

Comparison table

| Hallucination ❌ | Faithfulness ✅ |
| ----- | ----- |
| Makes up information | Uses only retrieved data |
| Sounds confident but wrong | Correct and grounded |
| Adds unrelated steps | Sticks to context |
| Reduces trust | Builds trust |

---

💡 Short summary

“Hallucination is when the model guesses; faithfulness is when it sticks to the data.”

