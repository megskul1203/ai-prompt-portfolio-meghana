#### **\*\*Day 67 \- MODEL MONITORING\*\***

####  

**\=== DAY 67: MODEL MONITORING \+ DRIFT \===**

Current portfolio: ai-prompt-portfolio-meghana (66/90 skills)  
Day 66: CI/CD for AI systems ✓  
Goal: Day 67/90 → Monitor Freddy AI after deployment

GIVE ME:

1\. Model monitoring setup  
2\. Types of drift  
3\. What metrics to watch  
4\. One Freshworks example  
5\. One table for drift types and signals  
6\. A short template for Day67\_ModelMonitoring.md

\#\#\# Example scenario  
Freddy AI is live, but answers are slowly getting worse.

\#\#\# Output format  
\# Day 67: Model Monitoring \+ Drift

\#\# Monitoring flow  
\- Track latency  
\- Track accuracy  
\- Track hallucination  
\- Track user feedback

\#\# Types of drift  
\- Data drift  
\- Concept drift  
\- Retrieval drift

\#\# Freshworks example  
\[one short example\]

\#\# Drift types  
| Drift type | Signal |  
|---|---|  
| Data drift | input changes |  
| Concept drift | target behavior changes |  
| Retrieval drift | wrong KB results |

\#\# Key idea  
\[one line only\]

**RESPONSE:**

Day 67: Model Monitoring \+ Drift  
---

Monitoring flow

* Track **latency** (response time)  
* Track **accuracy** (are answers correct)  
* Track **hallucination** (any made-up info)  
* Track **user feedback** (CSAT, thumbs up/down)

---

Types of drift

* **Data drift** → input data changes  
* **Concept drift** → correct answers change over time  
* **Retrieval drift** → system fetches wrong or outdated chunks

---

Freshworks example

🧾 Scenario:

Freddy AI is live, but answers are slowly getting worse

* Monitoring shows:  
  * CSAT dropping  
  * More incorrect answers  
* Investigation:  
  * New tickets use updated terms not present in KB  
* Issue → **data drift \+ retrieval drift**  
* Action:  
  * Update KB  
  * Re-embed data  
  * System performance improves

---

Drift types

| Drift type | Signal |
| ----- | ----- |
| Data drift | input queries change (new patterns, new terms) |
| Concept drift | correct answers change over time |
| Retrieval drift | wrong or outdated KB results retrieved |

---

📄 Template: Day67\_ModelMonitoring.md

\# Day 67: Model Monitoring \+ Drift

\#\# Monitoring Flow  
\- Track latency  
\- Track accuracy  
\- Track hallucination  
\- Track user feedback

\#\# Drift Types  
\- Data drift  
\- Concept drift  
\- Retrieval drift

\#\# Example  
Freddy AI answers degrade over time.  
CSAT drops → drift detected → KB updated → performance improves.

\#\# Key Idea  
Monitor continuously to detect and fix drift early

---

💡 Key idea

AI systems must be continuously monitored because performance can degrade over time.

