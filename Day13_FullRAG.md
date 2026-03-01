\#\#\*\*Day 13: Full RAG Pipeline\*\* \- Freshworks Freddy \+ Postman validation\!

**Prompt:**   
You are Freshworks Freddy RAG Pipeline (Days 11+12 integrated).

\*\*VECTOR DB \+ Postman Validation:\*\*  
\`\`\`  
Doc1: Freshdesk SLA escalation \[0.94\]    
Doc2: Freddy intent detection \[0.89\]  
Doc5: Postman API validation \[0.85\]  
\`\`\`

\*\*USER WORKFLOW:\*\*  
1\. Query: "Freshdesk SLA policy \+ API test after ticket fix"  
2\. \*\*Vector Retrieval:\*\* Top 3 docs \+ scores  
3\. \*\*Freddy RAG Answer:\*\* Grounded response  
4\. \*\*Postman Validation:\*\* Newman CLI test suite for fix  
5\. \*\*Pipeline Confidence:\*\* End-to-end 1-10

\*\*OUTPUT FORMAT:\*\*  
Retrieval: \[Doc1 0.94, ...\]  
Freddy Answer: \[...\]  
Postman Tests: \[Newman script\]  
Confidence: 9/10  
\`\`\`

**Response:**

**Retrieval:**  
Doc1 – 0.94  
Doc2 – 0.89  
Doc5 – 0.85

---

Freddy Answer (Grounded on Retrieved Docs Only)

Based on:

* **Doc1: Freshdesk SLA escalation**  
* **Doc2: Freddy intent detection**  
* **Doc5: Postman API validation**

🔹 Freshdesk SLA Policy

High-priority tickets follow an SLA-driven escalation workflow:

1. **SLA Rules Applied**  
   * Response and resolution timers defined per priority.  
   * High-priority tickets have stricter thresholds.  
2. **Escalation Logic**  
   * If SLA breach is imminent or exceeded:  
     * Ticket escalates to next-level support group.  
     * Notifications triggered to stakeholders.  
3. **Freddy Intent Detection**  
   * Freddy detects urgency signals in ticket content.  
   * Automatically categorizes as high-priority.  
   * Triggers SLA policy and escalation workflow.

🔹 API Test After Ticket Fix

After resolving the ticket:

1. Trigger API validation suite (Postman collection).  
2. Validate:  
   * Status codes (200/4xx/5xx as expected)  
   * Response schema integrity  
   * Business logic correctness  
3. If tests fail:  
   * Reopen ticket  
   * Attach failure logs

This ensures SLA compliance is backed by functional API validation before final closure.

---

Postman Tests (Newman CLI Suite)

\# Install Newman (if not installed)  
npm install \-g newman

\# Run SLA Fix Validation Collection  
newman run Freshdesk\_SLA\_Fix\_Validation.postman\_collection.json \\  
  \-e production\_environment.postman\_environment.json \\  
  \--reporters cli,html \\  
  \--reporter-html-export SLA\_Fix\_Report.html

Sample Postman Test Script (Inside Collection)  
pm.test("Status code is 200", function () {  
    pm.response.to.have.status(200);  
});

pm.test("Response time \< 500ms", function () {  
    pm.expect(pm.response.responseTime).to.be.below(500);  
});

pm.test("SLA escalation field updated", function () {  
    var jsonData \= pm.response.json();  
    pm.expect(jsonData.sla\_status).to.eql("active");  
});

This validates:

* Fix deployed correctly  
* SLA logic intact  
* Escalation metadata consistent

---

Confidence: 9/10

**Breakdown:**

* Retrieval relevance: High (SLA \+ intent \+ validation aligned)  
* SLA coverage: Strong  
* API regression validation: Present  
* End-to-end workflow integrity: Covered

End-to-end pipeline reliability: **9/10**

