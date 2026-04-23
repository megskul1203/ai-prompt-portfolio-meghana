#### **\*\*Day 66 \- CI/CD FOR AI SYSTEMS\*\***

**\=== DAY 66: CI/CD FOR AI SYSTEMS \===**

Current portfolio: ai-prompt-portfolio-meghana (65/90 skills)  
Day 65: Canary deployment \+ rollback ✓  
Goal: Day 66/90 → CI/CD pipeline for Freddy AI updates

GIVE ME:

1\. CI/CD pipeline structure for AI systems  
2\. What gets tested before deployment  
3\. One Freshworks example  
4\. One table of CI vs CD stages  
5\. A short template for Day66\_AICICD.md

\#\#\# Example scenario  
A new Freddy AI model is ready for deployment.

\#\#\# Output format  
\# Day 66: CI/CD for AI Systems

\#\# CI/CD flow  
\- Code change  
\- Tests  
\- Evaluation  
\- Canary deploy  
\- Monitoring  
\- Full rollout

\#\# What gets checked  
\- Retrieval quality  
\- Faithfulness  
\- Latency  
\- Cost  
\- Safety

\#\# Freshworks example  
\[one short example\]

\#\# CI vs CD  
| CI | CD |  
|---|---|  
| test changes | deploy changes |  
| catch errors early | release safely |

\#\# Key idea  
\[one line only\]

**RESPONSE:**  
CI/CD flow

* **Code / model change** (new Freddy AI version)  
* **Run tests** (basic checks)  
* **Run evaluation** (RAG metrics)  
* **Canary deploy** (small % users)  
* **Monitor metrics** (latency, CSAT, errors)  
* **Full rollout** (if everything is stable)

---

What gets checked

* **Retrieval quality** → are correct chunks fetched  
* **Faithfulness** → answer sticks to data  
* **Latency** → response time within limit  
* **Cost** → not too expensive  
* **Safety** → no harmful or wrong responses

---

Freshworks example

🧾 Scenario:

A new Freddy AI model is ready for deployment

* Code \+ model updated  
* Tests run → pass  
* Evaluation shows good retrieval \+ low hallucination  
* Canary release to **5% users**  
* Monitoring:  
  * Latency stable  
  * CSAT improved  
* Decision → **full rollout to 100% users**

---

CI vs CD

| CI | CD |
| ----- | ----- |
| test changes | deploy changes |
| catch errors early | release safely |
| runs on every update | runs after tests pass |
| ensures quality | ensures stability |

---

📄 Template: Day66\_AICICD.md

\# Day 66: CI/CD for AI Systems

\#\# CI/CD Flow  
\- Code/model change  
\- Run tests  
\- Run evaluation  
\- Canary deployment  
\- Monitor metrics  
\- Full rollout

\#\# Checks  
\- Retrieval quality  
\- Faithfulness  
\- Latency  
\- Cost  
\- Safety

\#\# Example  
New Freddy AI model tested → evaluated → deployed to 5% users → monitored → rolled out fully.

\#\# Key Idea  
Test first, deploy safely

---

💡 Key idea

CI/CD ensures AI systems are tested, safe, and stable before full release.

