#### **\*\*Day 66 \- CANARY DEPLOYMENT\*\***

**\=== DAY 65: CANARY DEPLOYMENT \+ ROLLBACK \===**

Current portfolio: ai-prompt-portfolio-meghana (64/90 skills)  
Day 64: RAG evaluation framework ✓  
Goal: Day 65/90 → Safe release strategy for Freddy AI updates

GIVE ME:

1\. Canary deployment flow  
2\. Rollback strategy  
3\. One Freshworks production example  
4\. One table comparing canary vs full release  
5\. A short template for Day65\_CanaryRollback.md

\#\#\# Example scenario  
New Freddy AI version improves resolution but may increase latency.

\#\#\# Output format  
\# Day 65: Canary Deployment \+ Rollback

\#\# Canary flow  
\- Release to 1% traffic  
\- Monitor latency, accuracy, CSAT  
\- Expand to 10%, 50%, 100% if safe

\#\# Rollback strategy  
\- Roll back if latency increases  
\- Roll back if hallucination rises  
\- Roll back if CSAT drops

\#\# Freshworks example  
\[one short example\]

\#\# Canary vs full release  
| Canary | Full release |  
|---|---|  
| small risk | big risk |  
| gradual rollout | immediate rollout |

\#\# Key idea  
\[one line only\]

**RESPONSE:**

Canary flow

👉 Canary \= **release to a small group first, then expand slowly**

* Release to **1% traffic**  
* Monitor:  
  * Latency  
  * Accuracy  
  * CSAT  
* If stable → increase to **10% → 50% → 100%**  
* If issues → stop rollout

---

Rollback strategy

👉 Rollback \= **go back to old version quickly if something breaks**

* Roll back if **latency increases**  
* Roll back if **hallucination rises**  
* Roll back if **CSAT drops**  
* Switch traffic back to previous stable version (fast)

---

Freshworks example

🧾 Scenario:

New Freddy AI version improves resolution but may increase latency

---

🟢 Canary rollout:

* 1% users → test new version  
* Monitor:  
  * Response time  
  * Answer quality

---

⚠️ Issue detected:

* Latency increased from **1.2s → 2.0s**

---

🔁 Rollback:

* Traffic shifted back to old version  
* Users unaffected

---

Canary vs full release

| Canary | Full release |
| ----- | ----- |
| small risk | big risk |
| gradual rollout | immediate rollout |
| easy rollback | harder rollback |
| real user testing | no early validation |

---

📄 Template: Day65\_CanaryRollback.md

\# Day 65: Canary Deployment \+ Rollback

\#\# Canary Flow  
\- Release to 1% users  
\- Monitor latency, accuracy, CSAT  
\- Gradually increase traffic

\#\# Rollback Strategy  
\- Roll back if latency increases  
\- Roll back if hallucination increases  
\- Roll back if CSAT drops

\#\# Example  
New Freddy AI version deployed to 1% users.  
Latency increased → rollback triggered → system stable.

\#\# Key Idea  
Release slowly, rollback quickly

---

💡 Key idea

Deploy slowly to reduce risk, and always be ready to roll back fast.

