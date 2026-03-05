#### **\*\*Day 17: Agentic RAG \- Multi-Agent Systems\*\*** 

#### **\#\# \*\*Mission: Autonomous Freshworks Ticket Resolution\*\***

\`\`\`  
Goal: RAG → Self-improving agent swarm  
Production: Freddy AI agents resolve 70% tickets autonomously  
\`\`\`

\`\`\`  
**Prompt:**   
You are Freshworks Agentic RAG Swarm (4 specialized agents).

\*\*AGENTS:\*\*  
1\. \*\*Retrieval Agent:\*\* Vector search Freshworks KB  
2\. \*\*Reasoning Agent:\*\* ToT analysis of retrieved docs  
3\. \*\*Action Agent:\*\* Freddy auto-resolve \+ Postman test  
4\. \*\*Critic Agent:\*\* Validate resolution → Escalate if needed

\*\*TICKET:\*\* "Freshdesk SLA breach \- API fix required"

\*\*AGENT WORKFLOW:\*\*  
1\. Retrieval: Top 3 docs \+ scores  
2\. Reasoning: ToT 3 options for resolution  
3\. Action: Freddy response \+ Newman test script  
4\. Critic: Resolution quality 1-10 \+ escalate?

\*\*OUTPUT:\*\*  
Retrieval: \[...\]  
Reasoning: \[...\]  
Action: \[...\]  
Critic: 9/10 ![✅][image1] Autonomous resolution  
\`\`\`

**Response:**

🤖 Freshworks Agentic RAG Swarm Resolution

**Ticket:** *“Freshdesk SLA breach – API fix required”*

---

1️⃣ Retrieval Agent (Vector Search – Freshworks KB)

**Top 3 Retrieved Docs**

1. Freshdesk – *SLA Breach Automation & Escalation Rules* → **\[0.93\]**  
2. Freshdesk – *Freshdesk Ticket Update API & Priority Management* → **\[0.90\]**  
3. Freddy AI – *Freddy AI Auto-Resolve & Suggested Actions* → **\[0.88\]**

**Insight**

Relevant docs connect:

* SLA breach detection  
* Ticket update API  
* Freddy AI auto-resolution suggestions

---

2️⃣ Reasoning Agent (Tree-of-Thought Analysis)

🌳 Option 1 — Manual SLA Escalation

* Supervisor notified  
* Ticket reassigned to escalation group

**Pros:** Fast operational response  
**Cons:** Does not fix root API issue

---

🌳 Option 2 — API Patch \+ Ticket Update

* Use Freshdesk API to update ticket priority  
* Trigger escalation workflow

**Pros:** Fixes root issue  
**Cons:** Requires API validation

---

🌳 Option 3 — Freddy AI Assisted Resolution

* Freddy analyzes ticket context  
* Suggests API fix  
* Executes automated update workflow

**Pros:** Autonomous \+ scalable  
**Cons:** Requires validation via API testing

✅ **Selected Strategy:** **Option 3 (AI-assisted automated fix)**

---

3️⃣ Action Agent  
🤖 Freddy AI Response

Freddy AI detects SLA breach caused by delayed API update.

Automated actions:

1. Increase ticket priority to **Urgent**  
2. Assign to **API Support Group**  
3. Add AI-generated summary for engineers  
4. Trigger API health test

---

🔧 Freshdesk API Fix (Example)

PATCH /api/v2/tickets/{ticket\_id}

{  
 "priority": 4,  
 "status": 2,  
 "group\_id": 820001  
}

Purpose:

* Escalate priority  
* Move ticket to API support team

---

🧪 Postman / Newman Test Script

newman run freshdesk\_api\_test.json \\  
\--env-var base\_url=https://company.freshdesk.com \\  
\--env-var api\_key=$FRESHDESK\_API\_KEY \\  
\--reporters cli

Test checks:

* Ticket update endpoint response  
* SLA priority update success  
* Escalation workflow triggered

---

4️⃣ Critic Agent (Validation)

🔍 Evaluation

| Metric | Score |
| ----- | ----- |
| Retrieval relevance | 9/10 |
| Reasoning quality | 9/10 |
| Automation completeness | 9/10 |
| Resolution reliability | 9/10 |

📊 Final Score

**9 / 10**

✅ **Autonomous Resolution Successful**  
❌ Escalation Not Required

---

🔁 Final Agentic Flow

Vector Retrieval  
→ Tree-of-Thought Reasoning  
→ Freddy AI Auto-Action  
→ API Validation via Newman  
→ Critic Quality Check

**Outcome:** SLA breach mitigated and API workflow verified automatically.

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAARCAMAAAAMs7fIAAADAFBMVEUAAAB8s0J8s0J8s0Jonzhonzhonzh8s0Jonzh8s0JonzhonzhonzhtpDtonzhonzhonzhonzhonzh8s0J6sUF1rD5sozponzh7skGGuVCJulSQv1+LvFeEt01/tEafx3SkynuTwGJtpDuiyXeYw2mdxnCBtkmcxXDL37Tb6MvT48C00pKaxG37+fnz9e6UwGSMvFmOvVvr8OLj7NeszYekyXvD2qm81p54r0BxqDx2rT93rkBrojkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAApjS7yAAAAE3RSTlMAUK/vv4AQgM8wnzBAgHDvII9g5u0TdAAAAINJREFUeF5VzUEOgkAMBdBfZ4iEuNAVho0uOAP3PwgbjBpYk7hQSGg7QGuTn0lf8juEcIabONDxlGcYHR0AByWHxaAKN5XLDkCn8jCQhqS6C9ScZ5IrviIf4C0vS791FLQl6w7bLf61SKDC935A60Rn7axCDpK8ZgNQ1tgCuUaIf4JpAUEvF0I4QOOaAAAAAElFTkSuQmCC>