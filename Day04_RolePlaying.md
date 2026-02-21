**Role Playing Prompts**

**1\. Content Strategist**

You are a senior content strategist with 5+ years of experience. Write a LinkedIn post announcing "Day 4/90 AI Prompt Engineering journey \- mastered role-playing prompts". 150 words, 3 stats, CTA to connect. 

Response:

**Day 4/90 of My AI Prompt Engineering Journey**

Today I mastered **role-playing prompts**—a technique that makes AI respond like a specific expert (content strategist, developer, marketer, or educator). As a content strategist, I see this as giving AI a clear persona and objective—just like defining a brand voice or audience persona.

**3 Key Insights:**  
 • Role-based prompts can increase output relevance by **50–60%**  
 • Structured context reduces revision time by **30–40%**  
 • Persona-driven prompts can **2x clarity and tone consistency**

This approach is reshaping how I think about content creation—prompts are becoming strategic frameworks, not just questions.

If you’re exploring AI, content strategy, or prompt engineering, let’s connect and exchange insights\!

\#AI \#PromptEngineering \#ContentStrategy \#LearningInPublic \#LinkedInJourney

**2\. Product Manager (₹12L company)** 

You are Freshworks AI Product Manager.  Write user story \+ 3 acceptance criteria for "AI prompt playground" tool.

Response:

**User Story (AI Prompt Playground)**  
 As an AI Product Manager at Freshworks, I want a prompt playground where users can experiment with prompts, roles, and parameters in real time so that they can quickly test, refine, and deploy high-quality AI prompts for their workflows.

**Acceptance Criteria**

1. **Prompt Testing Interface:** Users can enter prompts, select roles (system/user/assistant), and adjust parameters (temperature, max tokens) with real-time response preview.

2. **Versioning & History:** Users can save, edit, and compare multiple prompt versions, with a history log of outputs and configurations.

3. **Export & Integration:** Users can export finalized prompts as JSON/API-ready formats and integrate them into Freshworks AI workflows or products with one click.

**3\. Tech Interviewer** 

You are Google Prompt Engineer interviewer. Ask 3 behavioral questions for ₹12 LPA role. Wait for the answer. 

Response:

Great. I’ll act as the **Google Prompt Engineer interviewer**.  
 Please answer these **3 behavioral questions** as you would in an interview:

**1\. Learning & Adaptability**  
 Tell me about a time you had to quickly learn a new technical skill or tool. How did you approach it, and what was the outcome?

**2\. Problem Solving Under Pressure**  
 Describe a situation where something you built or wrote (code, content, prompt, project) failed or didn’t work as expected. How did you diagnose and fix it?

**3\. Collaboration & Communication**  
 Give an example of how you explained a complex concept (technical or non-technical) to someone with less knowledge. How did you ensure they understood?

**4\. Upwork Freelancer** 

You are top 1% Upwork AI specialist. Write ₹50k proposal for "Build AI content generator for SaaS".  

Response:

Here’s a **high-converting ₹50,000 Upwork proposal** tailored for a SaaS AI content generator project 👇

**Proposal: Build AI Content Generator for SaaS**

Hello,

I’m a top-rated AI specialist and content strategist with 5+ years of experience designing scalable content systems for SaaS products. I specialize in **prompt engineering, AI workflows, and developer-friendly tools** that turn LLMs into real business assets.

✅ What I Will Build

A custom **AI Content Generator** tailored to your SaaS workflows, capable of:

* Generating blogs, landing pages, product descriptions, emails, and social media content  
* Maintaining consistent brand voice using structured prompt frameworks  
* Role-based generation (SEO expert, marketer, PM, developer)  
* Adjustable parameters (tone, length, audience, creativity level)  
* Pre-built templates for repeatable content production

🧠 Tech Approach

* OpenAI / Claude / Gemini API integration  
* Backend: Python (FastAPI) or Node.js  
* Frontend: Streamlit or React-based UI  
* Prompt library \+ reusable prompt architecture  
* Optional: RAG with vector database for brand knowledge

📦 Deliverables

* Fully functional AI content generator web app  
* Prompt templates \+ documentation  
* Deployment guide (local/cloud)  
* 2 weeks post-delivery support

💡 Why Hire Me

* Strong blend of content strategy \+ AI engineering  
* Focus on real SaaS use cases, not generic demos  
* Clear documentation and maintainable code  
* Fast delivery with structured milestones

💰 **Fixed Price:** ₹50,000  
⏱ **Timeline:** 7–14 days

Let’s discuss your SaaS use case and tailor the generator to your brand and workflows.

Best regards,  
**Meghana**

**5\. Code Reviewer** 

You are Senior Python Developer. Review this prompt engineering utility: def classify\_email(text): prompt \= f"Classify as spam/not spam: {text}" return call\_llm(prompt) Suggest 3 improvements.

Response:

As a senior Python developer, here are **3 key improvements** to make this prompt utility more robust and production-ready:

1\) Add Structured Prompting (Reduce Ambiguity)

The current prompt is too vague and may return long explanations. Force a strict output format.

**Improvement:**

prompt \= f"""

You are an email spam classifier.

Respond ONLY with: "spam" or "not spam".

Email:

{text}

"""

2\) Handle Injection & Truncation Risks

User input could inject instructions (prompt injection). Wrap input safely and limit length.

**Improvement:**

safe\_text \= text\[:2000\]  \# truncate long emails

3\) Add Post-Processing & Validation

LLMs can return unexpected text. Validate output before returning.

**Improvement:**

result \= call\_llm(prompt).strip().lower()

return "spam" if "spam" in result else "not spam"

Bonus (Senior-Level Enhancement)

Use **few-shot examples** for higher accuracy:

prompt \= """

Classify emails as spam or not spam.

Example:

"Win free money now\!" \-\> spam

"Meeting at 3pm" \-\> not spam

Email: {text}

Output:

"""

