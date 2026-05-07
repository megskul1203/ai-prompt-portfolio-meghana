# Meghana's 90-Day AI Engineer Journey
### Bengaluru → Production AI Engineering → ₹12–18 LPA

![Progress](https://img.shields.io/badge/Day-79%20of%2090-brightgreen)
![Phase](https://img.shields.io/badge/Phase-4%20In%20Progress-blue)
![Code Days](https://img.shields.io/badge/Real%20Code-Days%2069--79-orange)
![Live Apps](https://img.shields.io/badge/Live%20Apps-2%20Deployed-success)

---

## 🚀 Live Applications

> These are real, deployed AI applications — not just code files. Click and try them.

| App | What It Does | Link |
|---|---|---|
| 🧠 RAG Pipeline | Ask questions answered from a real knowledge base — no hallucination | [Try it live →](https://meghana-rag-pipeline.streamlit.app) |
| 📚 Course Generator | Generate complete course outlines using instructional design principles | [Try it live →](https://meghana-course-generator.streamlit.app) |

---

## About This Journey

I'm Meghana — a Content Developer (L&D) in Bengaluru, actively transitioning into AI Engineering. This repository documents my daily progression from AI concept study to deployed, production-style AI applications.

**Background:** CS Engineering degree → 3 years UPSC prep → Content Developer (L&D) → AI Engineer in training.

Days 1–68 were deep concept study. Days 69+ are real running Python code, committed and deployed daily.

**What makes this portfolio different:** I don't just know AI concepts — I've built and deployed working applications that combine L&D domain expertise with AI engineering. Every project below has a real `.py` file that runs.

---

## 🏆 Key Achievements

| Milestone | What I Built | Day |
|---|---|---|
| First real API call | Groq + Python, env variables, git push | Day 69 |
| Prompt templates | f-strings, loops, 5 AI explanations in one run | Day 70 |
| AI Content Reviewer | Reads file → AI review → saves output automatically | Day 71 |
| Chatbot with memory | Stateful conversation via full history trick | Day 72 |
| Semantic search | Embeddings + cosine similarity, local model | Day 73 |
| Vector database | ChromaDB, 12 docs, 4 semantic queries | Day 74 |
| **Complete RAG pipeline** | ChromaDB + Groq end-to-end, hallucination prevention | **Day 75** |
| **Streamlit web app** | RAG pipeline wrapped in a live browser UI | **Day 76** |
| **Deployed to public URL** | Live on Streamlit Community Cloud, shareable link | **Day 77** |
| **AI Course Generator** | L&D expertise + AI engineering in one deployed tool | **Day 78** |
| **RAG Evaluation** | Custom LLM-as-a-judge: faithfulness, relevancy, precision | **Day 79** |

---

## 🛠 Tech Stack

| Layer | Tools |
|---|---|
| Language | Python 3.14 |
| LLM API | Groq (llama-3.3-70b-versatile) |
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) — local, free |
| Vector DB | ChromaDB with cosine similarity |
| UI Framework | Streamlit |
| Deployment | Streamlit Community Cloud |
| Evaluation | Custom LLM-as-a-judge (faithfulness, relevancy, precision) |

---

## 📁 Real Code Projects (Days 69–79)

> Every row below is a real Python file that runs. No placeholder entries.

| Day | What I Built | Python File | Reflection |
|---|---|---|---|
| 69 | First real AI API call | [day69_api.py](day69_api.py) | [View](Day69_PythonReboot.md) |
| 70 | Prompt templates with f-strings + loops | [day70_prompt_templates.py](day70_prompt_templates.py) | [View](Day70_PromptTemplates.md) |
| 71 | AI content reviewer (reads file → AI → saves output) | [day71_content_reviewer.py](day71_content_reviewer.py) | [View](Day71_ContentReviewer.md) |
| 72 | Chatbot with memory (full conversation history) | [day72_chatbot.py](day72_chatbot.py) | [View](Day72_Chatbot.md) |
| 73 | Semantic search with embeddings + cosine similarity | [day73_embeddings.py](day73_embeddings.py) | [View](Day73_Embeddings.md) |
| 74 | ChromaDB vector database (12 docs, 4 semantic queries) | [day74_chromadb.py](day74_chromadb.py) | [View](Day74_ChromaDB.md) |
| 75 | **Complete RAG pipeline** (ChromaDB + Groq, hallucination prevention) | [day75_rag_pipeline.py](day75_rag_pipeline.py) | [View](Day75_RAGPipeline.md) |
| 76 | **Streamlit UI** wrapping the RAG pipeline | [day76_streamlit_rag.py](day76_streamlit_rag.py) | [View](Day76_StreamlitUI.md) |
| 77 | **Deployed** RAG pipeline to public URL | — | [View](Day77_Deployment.md) |
| 78 | **AI Course Generator** — L&D + AI in one deployed app | [day78_course_generator.py](day78_course_generator.py) | [View](Day78_CourseGenerator.md) |
| 79 | **RAG Evaluation** — custom LLM-as-a-judge scoring | [day79_rag_evaluation.py](day79_rag_evaluation.py) | [View](Day79_Evaluation.md) |

---

## 📊 RAG Pipeline Evaluation Results

> Evaluated using a custom LLM-as-a-judge framework (Day 79)

| Question | Faithfulness | Answer Relevancy | Context Precision |
|---|---|---|---|
| What is RAG? | 1.00 ✅ | 1.00 ✅ | 1.00 ✅ |
| How does Freshworks use RAG? | 1.00 ✅ | 0.80 ✅ | 0.80 ✅ |
| What are RAG evaluation metrics? | 0.50 | 0.00 | 0.80 ✅ |
| What is the capital of France? | 1.00 ✅ | 0.00 ✅ | 0.00 ✅ |
| **Average (in-scope questions)** | **1.00** | **0.90** | **0.90** |

*Note: Question 4 scores 0 on relevancy/precision correctly — the pipeline refused to hallucinate about a topic not in its knowledge base. This is intended behaviour.*

---

## 📚 Theory Foundation (Days 1–68)

<details>
<summary>Click to expand — 68 days of AI concept study</summary>

### Phase 1 — Prompt Engineering Foundations (Days 1–10) ✅

| Day | Skill | File |
|---|---|---|
| 01 | Zero-shot prompting | [View](Day01_ZeroShot.md) |
| 02 | Model parameters mastery | [View](Day02_Parameters.md) |
| 03 | Few-shot prompting | [View](Day03_FewShot.md) |
| 04 | Role-playing prompts | [View](Day04_RolePlaying.md) |
| 05 | Prompt chaining | [View](Day05_Chaining.md) |
| 06 | Chain-of-thought reasoning | [View](Day06_CoT.md) |
| 07 | Week 1 review | [View](Day07_Review.md) |
| 08 | Tree-of-thought prompting | [View](Day08_ToT.md) |
| 09 | ToT with Postman | [View](Day09_PostmanToT.md) |
| 10 | Enterprise ToT applications | [View](Day10_EnterpriseToT.md) |

### Phase 2 — RAG & Developer Skills (Days 11–30) ✅

| Day | Skill | File |
|---|---|---|
| 11 | RAG basics | [View](Day11_RAG.md) |
| 12 | Vector search | [View](Day12_VectorSearch.md) |
| 13 | Full RAG pipeline | [View](Day13_FullRAG.md) |
| 14 | RAG metrics | [View](Day14_RAGMetrics.md) |
| 15 | Fine-tuned RAG | [View](Day15_FineTunedRAG.md) |
| 16 | Week 2 review | [View](Day16_Week2Review.md) |
| 17 | Agentic RAG | [View](Day17_AgenticRAG.md) |
| 18 | 90 skills mapping | [View](Day18_90Skills.md) |
| 19 | Hybrid RAG | [View](Day19_HybridRAG.md) |
| 20 | Agent memory | [View](Day20_AgentMemory.md) |
| 21 | Hybrid RAG evaluation | [View](Day21_HybridRAG_Eval.md) |
| 22 | Multi-modal RAG | [View](Day22_MultiModalRAG.md) |
| 23 | Agentic RAG advanced | [View](Day23_AgenticRAG.md) |
| 24 | Observability | [View](Day24_Observability.md) |
| 25 | Multi-agent systems | [View](Day25_MultiAgent.md) |
| 26 | Self-healing RAG | [View](Day26_SelfHealingRAG.md) |
| 27 | Cost optimization | [View](Day27_CostOptimization.md) |
| 28 | A/B testing prompts | [View](Day28_ABTesting.md) |
| 29 | RAGAS benchmark | [View](Day29_RAGASBenchmark.md) |
| 30 | Transformers theory | [View](Day30_TransformersTheory.md) |

### Phase 3 — Production Mastery (Days 31–68) ✅

| Day | Skill | File |
|---|---|---|
| 31 | RAG architecture | [View](Day31_RAGArchitecture.md) |
| 32 | LLM evaluation framework | [View](Day32_LLMEval.md) |
| 33 | Advanced reasoning | [View](Day33_AdvancedReasoning.md) |
| 34 | Monitoring dashboard | [View](Day34_MonitoringDashboard.md) |
| 35 | Production RAG pipeline | [View](Day35_ProductionRAG.md) |
| 36 | LLM eval framework v2 | [View](Day36_LLM_EvalFramework.md) |
| 37 | AI platform design | [View](Day37_AIPlatformDesign.md) |
| 38 | Product case study | [View](Day38_ProductCaseStudy.md) |
| 39 | Leadership cases | [View](Day39_LeadershipCases.md) |
| 40 | Freddy AI system design | [View](Day40_FreddySystemDesign.md) |
| 41 | Cost optimisation | [View](Day41_CostOptimization.md) |
| 42 | Multi-region HA | [View](Day42_MultiRegionHA.md) |
| 43 | RAG drift detection | [View](Day43_RAGDrift.md) |
| 44 | Multi-modal RAG advanced | [View](Day44_MultiModalRAG.md) |
| 45 | L1 automation | [View](Day45_L1Automation.md) |
| 46 | GraphRAG | [View](Day46_GraphRAG.md) |
| 47 | Agentic workflow | [View](Day47_AgenticWorkflow.md) |
| 48 | Eval-driven development | [View](Day48_EvalDriven.md) |
| 49 | RLHF | [View](Day49_RLHF.md) |
| 50 | Platform roadmap | [View](Day50_PlatformRoadmap.md) |
| 51 | MLOps | [View](Day51_MLOps.md) |
| 52 | Feature flags | [View](Day52_FeatureFlags.md) |
| 53 | Data lineage | [View](Day53_DataLineage.md) |
| 54 | Circuit breaker pattern | [View](Day54_CircuitBreaker.md) |
| 55 | Blue-green deployments | [View](Day55_BlueGreen.md) |
| 56 | Service mesh | [View](Day56_ServiceMesh.md) |
| 57 | Vector indexing | [View](Day57_VectorIndex.md) |
| 58 | Chunking strategies | [View](Day58_Chunking.md) |
| 59 | RAG retrieval | [View](Day59_RagRetrieval.md) |
| 60 | Retrieval quality | [View](Day60_RetrievalQuality.md) |
| 61 | RAG evaluation | [View](Day61_Ragevaluation.md) |
| 62 | Hallucination detection | [View](Day62_Hallucinations.md) |
| 63 | RAG evaluation framework v1 | [View](Day63_RAGEvaluationFramework.md) |
| 64 | RAG evaluation framework v2 | [View](Day64_RAGEvaluationFramework.md) |
| 65 | Canary rollback | [View](Day65_CanaryRollback.md) |
| 66 | AI CI/CD | [View](Day66_AICICD.md) |
| 67 | Model monitoring | [View](Day67_ModelMonitoring.md) |
| 68 | Dataset versioning | [View](Day68_DatasetVersioning.md) |

</details>

---

## 🎯 Target Roles

| Role | Status | Salary Range |
|---|---|---|
| AI Technical Writer | Ready to apply now | ₹8–14 LPA |
| AI Curriculum Designer | Ready now — L&D background is the advantage | ₹10–16 LPA |
| Prompt Engineer | Live RAG demo ready | ₹10–18 LPA |
| AI Learning Experience Designer | Month 2 target | ₹16–24 LPA |

**Companies whose AI stack aligns with this work:** Freshworks · Postman · Hasura · Razorpay · Sprinklr · upGrad · Scaler · Yellow.ai · Observe.AI · Uniphore · Sarvam AI

---

## What's Coming

| Day | Goal |
|---|---|
| 80 | README update + portfolio polish |
| 81+ | Job applications with live demo links |

---

*Last updated: Day 79 complete — RAG pipeline evaluated, two apps live*
*Location: Bengaluru, Karnataka*