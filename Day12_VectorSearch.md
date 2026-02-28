<img width="1920" height="1020" alt="Vector Search 1" src="https://github.com/user-attachments/assets/717e5187-792b-4872-97b4-15b29e046be4" />
<img width="1920" height="1020" alt="Vector Search 2" src="https://github.com/user-attachments/assets/9f5e08dd-3899-4a77-93f4-50522a95665a" />
**\#\# \*\*Day 12 Mission: Freshworks KB → Vector Search\*\***

Goal: Convert docs → embeddings → cosine similarity → Top-K retrieval  
Production: Scale Day 11 from 3 docs → 10,000+ docs

You are Freshworks RAG vector search engine.

\*\***VECTOR DATABASE**\*\* (10 Freshworks docs as embeddings):  
\`\`\`  
Doc1: "Freshdesk ticketing labels auto-assign SLA" \[vec: 0.92\]  
Doc2: "Freddy AI intent detection auto-response" \[vec: 0.87\]    
Doc3: "Freshservice IT assets change approval" \[vec: 0.76\]  
Doc4: "Freshchat conversational AI bots" \[vec: 0.91\]  
... \[6 more docs\]  
\`\`\`

\*\*QUERY:\*\* "Freshdesk high-priority ticket escalation policy"

\*\*VECTOR SEARCH:\*\*  
1\. Compute cosine similarity ALL docs vs query  
2\. Return TOP 3 docs (similarity scores)    
3\. RAG answer using ONLY top 3  
4\. Retrieval quality: 1-10

\*\*OUTPUT:\*\*  
Top 3: Doc1\[0.94\], Doc2\[0.89\], Doc5\[0.82\]  
Answer: \[...\]  
Quality: 9/10

**Response:**

**Top 3:**  
Doc1 \[0.94\]  
Doc2 \[0.89\]  
Doc4 \[0.88\]

**Answer (Using ONLY Top 3 Docs):**

Based on retrieved documents:

From **Doc1** ("Freshdesk ticketing labels auto-assign SLA"):  
High-priority ticket escalation in Freshdesk is governed through **labels, auto-assignment, and SLA rules**. You can:

* Apply a *high-priority label* to incoming tickets.  
* Configure **auto-assign rules** to route these tickets to a dedicated priority support group.  
* Define **SLA policies** with stricter response and resolution targets to trigger escalation when breached.

From **Doc2** ("Freddy AI intent detection auto-response"):  
**Freddy AI** can detect urgent intent in ticket content and:

* Automatically categorize tickets as high priority.  
* Trigger predefined workflows or escalation logic.  
* Send automated acknowledgements while escalating internally.

From **Doc4** ("Freshchat conversational AI bots"):  
If tickets originate from chat, conversational AI bots can:

* Identify urgency signals during conversations.  
* Route high-priority cases into Freshdesk with escalation tags applied.

**Combined Escalation Policy Flow:**

1. Detect urgency (Freddy AI intent detection or bot signals).  
2. Apply high-priority label.  
3. Auto-assign to escalation group.  
4. Enforce SLA timers.  
5. Escalate when SLA thresholds are breached.

**Retrieval Quality:** 9/10

