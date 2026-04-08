#### **\*\*DAY 51: MLOPS FUNDAMENTALS (DAGSTER \+ ORCHESTRATION)\*\***

Current portfolio: ai-prompt-portfolio-meghana (50/90 skills)  
Day 50: Platform roadmap ✓ 3-year Freshworks vision  
Goal: Day 51/90 → MLOps orchestration basics (production pipelines)

**\*\*UNDERSTAND MLOPS ORCHESTRATION\*\*** (Dagster/Airflow for Freddy):

1\. \*\*Pipeline Orchestration Flow\*\*  
\`\`\`  
Daily Jobs:  
1\. KB Crawl → GraphRAG Update (Day46)  
2\. RLHF Feedback → Reward Model (Day49)  
3\. Agent Eval → Canary Deploy (Day48)  
4\. Multi-region Sync (Day42)  
\`\`\`

2\. \*\*Dagster Workflow\*\* (simplified)  
\`\`\`  
@job  
def freddy\_pipeline():  
    crawl\_kb() → build\_graphrag()  
    eval\_agents() → deploy\_canary()  
    sync\_regions()  
\`\`\`

3\. \*\*Key Benefits\*\* (Freshworks scale)  
\`\`\`  
Reliability: 99.9% job success  
Observability: Lineage \+ failures tracked  
Scheduling: Daily 2AM auto-run  
Scale: 100+ parallel pipelines  
\`\`\`

**RESPONSE:**

DAY 51: MLOPS FUNDAMENTALS (DAGSTER \+ ORCHESTRATION)

**Goal:** Understand how Freshworks-style platforms orchestrate ML workflows using **Dagster/Airflow**.

---

1\. PIPELINE ORCHESTRATION FLOW

Orchestration \= a scheduler \+ controller that runs ML tasks in the right order, with monitoring and retries.

Your daily jobs:

1\. KB Crawl → GraphRAG Update

* Crawl Freshdesk/Freshservice knowledge base  
* Ingest new articles  
* Rebuild embeddings  
* Update GraphRAG edges (Day 46 work)  
* Validate semantic drift

**Why needed?**  
→ Keeps Freddy AI answers fresh and relevant daily.

---

2\. RLHF Feedback → Reward Model Update

* Take user thumbs-up/down  
* Aggregate weekly signals  
* Re-train reward model (Day49)  
* Validate performance

**Why needed?**  
→ Model continuously aligns with real customer behaviour.

---

3\. Agent Eval → Canary Deploy

* Run automated multi-agent tests (Day48)  
* Compare new model vs current production baseline  
* If metrics pass threshold → perform **canary deploy** to 5% users  
* Monitor for regressions

**Why needed?**  
→ Safe rollout without breaking customer workflows.

---

4\. Multi-region Sync

* Sync S3/GCS buckets  
* Sync vector stores (Pinecone / Qdrant / Aurora)  
* Sync model versions across US → EU → APAC

**Why needed?**  
→ Freshworks runs global workloads → consistent model behaviour everywhere.

---

2\. DAGSTER WORKFLOW (Simplified Representation)

Dagster likes to break work into **ops** and connect them into **jobs**.

Ops (Tasks):

* crawl\_kb()  
* build\_graphrag()  
* eval\_agents()  
* deploy\_canary()  
* sync\_regions()

Pipeline Job:  
@job  
def freddy\_pipeline():  
    crawl\_kb() \>\> build\_graphrag()  
    eval\_agents() \>\> deploy\_canary()  
    sync\_regions()

What this really means:

* KB tasks run sequentially  
* Evaluation → Deployment also sequential  
* Region sync runs independently  
* Dagster handles:  
  * retries  
  * logging  
  * lineage  
  * alerts on failures  
  * scheduled runs

---

3\. KEY BENEFITS (Freshworks-Scale)

✔ Reliability: 99.9% job success

* Automatic detection of stuck/failed tasks  
* Auto-retry with exponential backoff  
* Idempotent jobs → safe re-runs

✔ Observability & Lineage

* Each job shows:  
  * inputs  
  * outputs  
  * upstream/downstream dependencies  
  * which step failed  
* Perfect for debugging complex RAG pipelines.

✔ Scheduling

* Runs daily at **2 AM IST**  
* Can add manual runs for debugging  
* Cron triggers possible

✔ Scale: 100+ ML pipelines in parallel

* Multiple models: Freddy, Freshchat, Freshservice  
* Hundreds of ops running in a distributed Dagster cluster  
* Metadata stored in Postgres \+ S3

