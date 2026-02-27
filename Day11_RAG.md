\# Day 11: RAG Basics \- Freshworks Freddy Agent

**\#\# RAG Demo**  
Query: "Auto-assign high-priority tickets Freshdesk?"  
Retrieved: Doc1 (ticketing), Doc2 (Freddy AI)

You are Freshworks Freddy RAG agent.

\*\*KNOWLEDGE BASE\*\* (Freshworks docs):  
\`\`\`  
Doc1: Freshdesk ticketing → Labels → Auto-assign → SLA rules  
Doc2: Freddy AI → Intent detection → Auto-responses → Escalation  
Doc3: Freshservice IT → Asset mgmt → Change requests → Approval workflows  
\`\`\`

\*\*USER QUERY:\*\* "How do I auto-assign high-priority tickets in Freshdesk?"

\*\*RAG PROCESS:\*\*  
1\. Retrieve TOP 2 relevant docs  
2\. Quote exact passages    
3\. Generate answer using ONLY retrieved docs  
4\. Confidence score 1-10 (based on doc relevance)

\*\*OUTPUT FORMAT:\*\*  
Retrieved: \[Doc1, Doc2\]  
Answer: \[RAG response\]  
Confidence: 9/10

**\#\# Response:**

**Retrieved:** \[Doc1, Doc2\]

**Quoted Passages:**

From **Doc1**:

"Freshdesk ticketing → Labels → Auto-assign → SLA rules"

From **Doc2**:

"Freddy AI → Intent detection → Auto-responses → Escalation"

**Answer (Using Retrieved Docs Only):**

To auto-assign high-priority tickets in Freshdesk:

1. Use **Labels** to tag incoming tickets as high priority.  
2. Configure **Auto-assign** rules within Freshdesk ticketing to route labeled tickets to the appropriate agent or group.  
3. Apply **SLA rules** to ensure high-priority tickets are handled within defined response and resolution timelines.  
4. Optionally, use **Freddy AI intent detection** to automatically identify high-priority issues based on ticket content.  
5. Configure **Escalation** rules to route critical tickets to senior agents if conditions are met.

This setup ensures high-priority tickets are automatically identified, assigned, and escalated when necessary.

**Confidence:** 9/10

