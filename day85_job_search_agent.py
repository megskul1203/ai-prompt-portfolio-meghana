import streamlit as st
import os
import json
import re
import requests
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
MODEL = "openai/gpt-oss-120b"

# ── Meghana's profile ─────────────────────────────────────────────────────────
MEGHANA_PROFILE = """
MEGHANA S KULKARNI
Instructional Designer  |  Curriculum Developer  |  eLearning Specialist
Bengaluru, Karnataka, India  |  +91 7022102233  |  megskul1203@gmail.com
linkedin.com/in/meghana-kulkarni-2a4538317   |   github.com/megskul1203
SUMMARY
Instructional Designer with 2+ years of experience designing scalable, outcome-aligned eLearning modules, interactive scripts, and Articulate Storyline courses for enterprise programs reaching 45,000+ employees. Expertise across full L&D lifecycles — from Training Needs Analysis (TNA) and storyboarding to SME collaboration and rollout management. Computer Science Engineering background paired with hands-on experience building generative AI tools — including retrieval-augmented generation (RAG) pipelines and agentic workflows — to automate curriculum design and learning-outcome mapping.
CORE SKILLS
Instructional Design & Methodology: ADDIE, SAM (Successive Approximation Model), Bloom's Taxonomy, Curriculum Development, Storyboarding, Script Writing, Training Needs Analysis (TNA), Assessment Design, Skill-Aligned Learning Outcomes
eLearning & Authoring Tools: Articulate Storyline 360, Vyond, Stepping Stone LMS, Microlearning Design, Video Production & QC, Canva, MS Office
AI-Enhanced L&D Capabilities: Prompt Engineering, RAG Pipelines, Agentic Workflows, AI Curriculum Tools (Streamlit/Python), LLM Content Evaluation, Workflow Automation
Stakeholder Management: SME Coordination, Executive Communications, Cross-Functional Project Leadership
AI INSTRUCTIONAL DESIGN PROJECTS
•	Bloom's Taxonomy Learning Path Generator: Built a Streamlit application using LLMs to auto-generate structured, skill-aligned, multi-tier learning plans mapped to Bloom's cognitive levels.
•	Integrated L&D Toolkit: Designed an all-in-one suite — AI Course Generator, Quiz & Flashcard Maker, and Prompt Improver — with reusable templates for instructional designers.
•	AI Job Search Agent (Agentic Workflow): Built an autonomous agent that pulls live job listings via API and ranks them against a candidate profile using LLM-based scoring.
Portfolio & demos: github.com/megskul1203/ai-prompt-portfolio-meghana
PROFESSIONAL EXPERIENCE
Content Developer  —  Bigbasket
October 2024 – Present  (Promoted from Content Writer, November 2025)  |  Bengaluru
•	Enterprise Curriculum Design: Leading design and production of a 38-module (~6 hours video + Articulate), skill-aligned process training curriculum, measured by scope covering 11,000+ G1 supply chain and delivery employees, by architecting modular learning outcomes and script templates in partnership with SCM and LMD SMEs (launching Sept 2026).
•	Company-Wide Onboarding Content: Delivered the highest-rated induction script in company history, measured by a 9.5/10 feedback score across 45,000+ employees, by designing outcome-driven induction modules (Spirit of BB and Competencies of BB) through iterative stakeholder review (Dec 2025).
•	Production Quality Standards: Ensured consistent, on-brief training video output, measured by successful delivery across 4 live production shoots, by setting script cueing and QC acceptance criteria and directing visual alignment with SCM and Last Mile Delivery (LMD) SMEs.
•	Agile Microlearning Delivery: Sustained continuous skill reinforcement for operational teams, measured by 2–3 modules shipped monthly, by designing fast-turnaround WhatsApp microlearning content tied to live process updates.
•	Proofread leadership communication videos before company-wide release; co-designed the 2025 company diary.
Content Writer Intern  —  IIM Skills
December 2023 – October 2024  |  Bengaluru
•	Wrote SEO-optimised articles across multiple content niches, achieving top search rankings for 100% of assigned articles.
•	Completed the Masters Course in Content Writing, certified by IIM Skills, covering structured writing, research, and audience-aware content development.
UPSC Civil Services Preparation  —  Self-Directed
May 2020 – June 2023
•	3 years of intensive, self-directed study for India's national civil services examination — built research, analytical writing, and complex-topic simplification skills that carried directly into instructional design and content.
EDUCATION
B.E. Computer Science Engineering  —  PDA College of Engineering, Gulbarga
2020
CERTIFICATIONS
The Complete Instructional Designer Course — Udemy   •  Certified Content Writer — IIM Skills   •  Google AI Essentials (5-course Specialization) — Coursera   •  Introduction to Technical Writing — Udemy 
Languages: English, Kannada, Hindi

"""

# ── Helpers ───────────────────────────────────────────────────────────────────
def call_ai(prompt: str, system: str = "You are an expert career coach.") -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user",   "content": prompt}
        ],
        temperature=0.5,
        max_tokens=1500
    )
    return response.choices[0].message.content

def extract_json(text: str):
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        return json.loads(match.group())
    return json.loads(text)

@st.cache_data(ttl=3600)  # Cache results for 1 hour — saves API calls
def fetch_jobs(query: str, location: str, num_pages: int = 1):
    """Fetch live jobs from JSearch API"""
    url = "https://jsearch.p.rapidapi.com/search"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }
    params = {
        "query": f"{query} in {location}",
        "num_pages": num_pages,
        "date_posted": "month",
        "country": "in"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        return []

def analyse_job_fit(job: dict) -> dict:
    """Use AI to analyse how well a job fits Meghana's profile"""
    job_text = f"""
    Title: {job.get('job_title', 'N/A')}
    Company: {job.get('employer_name', 'N/A')}
    Location: {job.get('job_city', 'N/A')}, {job.get('job_country', 'N/A')}
    Description: {job.get('job_description', 'N/A')[:1500]}
    """

    prompt = f"""
Analyse this job against Meghana's profile and respond ONLY with valid JSON:

Meghana's Profile:
{MEGHANA_PROFILE}

Job Details:
{job_text}

Respond ONLY with this JSON format, no extra text:
{{
  "fit_score": 75,
  "fit_summary": "one sentence why this is or isn't a good fit",
  "top_matching_skills": ["skill1", "skill2", "skill3"],
  "key_requirements": ["requirement1", "requirement2", "requirement3"],
  "salary_estimate": "12-16 LPA (estimated)",
  "apply_recommendation": "Strong Apply / Apply / Maybe / Skip",
  "one_line_pitch": "one sentence Meghana can use when applying to this specific role"
}}
"""
    try:
        raw = call_ai(prompt)
        return extract_json(raw)
    except:
        return {
            "fit_score": 0,
            "fit_summary": "Could not analyse",
            "top_matching_skills": [],
            "key_requirements": [],
            "salary_estimate": "Unknown",
            "apply_recommendation": "Review manually",
            "one_line_pitch": ""
        }

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Job Search Agent — Meghana",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 AI Job Search Agent")
st.caption("Live jobs from LinkedIn, Indeed & Glassdoor — ranked and analysed for YOUR profile")
st.divider()

# ── Search inputs ─────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3)
with col1:
    role_query = st.selectbox(
        "Target Role",
        [
            "AI Technical Writer",
            "Prompt Engineer",
            "AI Curriculum Designer",
            "Technical Writer",
            "AI Content Specialist",
            "LLM Trainer",
            "Conversational AI Designer",
            "AI Learning Designer"
        ]
    )
with col2:
    location = st.selectbox(
        "Location",
        ["Bangalore", "Bengaluru", "Remote India", "Hyderabad", "Mumbai", "Chennai"]
    )
with col3:
    num_results = st.selectbox("Number of Results", [5, 10, 15], index=1)

# Target companies filter
st.markdown("**Filter by Target Companies** (optional — leave blank to see all)")
company_filter = st.multiselect(
    "Show jobs only from these companies",
    ["Freshworks", "Postman", "Chargebee", "Razorpay", "Hasura",
     "upGrad", "Scaler", "Sprinklr", "Uniphore", "Yellow.ai",
     "Observe.AI", "Sarvam AI", "Zoho", "BrowserStack", "Simplilearn"],
    default=[]
)

min_fit_score = st.slider("Minimum Fit Score to show", 0, 100, 50)

search_btn = st.button("🚀 Find Jobs", type="primary")

# ── Results ───────────────────────────────────────────────────────────────────
if search_btn:
    if not RAPIDAPI_KEY:
        st.error("RAPIDAPI_KEY not found in .env file. Please add it.")
    else:
        with st.spinner(f"Searching for {role_query} jobs in {location}..."):
            jobs = fetch_jobs(role_query, location, num_pages=2)

        if not jobs:
            st.warning("No jobs found. Try a different role or location.")
        else:
            # Filter by company if selected
            

            if not jobs:
                st.warning(f"No jobs found from your selected companies. Try removing the company filter.")
            else:
                st.success(f"Found {len(jobs)} jobs. Analysing fit with your profile...")
                progress = st.progress(0)
                analysed_jobs = []

                for i, job in enumerate(jobs[:num_results]):
                    with st.spinner(f"Analysing job {i+1} of {min(len(jobs), num_results)}..."):
                        analysis = analyse_job_fit(job)
                        analysed_jobs.append({**job, **analysis})
                    progress.progress((i + 1) / min(len(jobs), num_results))

                # Filter by minimum fit score
                filtered = [j for j in analysed_jobs if j.get("fit_score", 0) >= min_fit_score]

                # Sort by fit score descending
                filtered.sort(key=lambda x: x.get("fit_score", 0), reverse=True)

                progress.empty()
                st.divider()

                if not filtered:
                    st.warning(f"No jobs scored above {min_fit_score}%. Try lowering the minimum fit score.")
                else:
                    st.subheader(f"🎯 {len(filtered)} Jobs Ranked by Fit Score")

                    for i, job in enumerate(filtered, 1):
                        score = job.get("fit_score", 0)
                        recommendation = job.get("apply_recommendation", "")

                        # Color code by recommendation
                        if "Strong" in recommendation:
                            indicator = "🟢"
                        elif recommendation == "Apply":
                            indicator = "🟡"
                        elif recommendation == "Maybe":
                            indicator = "🟠"
                        else:
                            indicator = "🔴"

                        with st.expander(
                            f"{indicator} #{i} — {job.get('job_title')} @ {job.get('employer_name')} — {score}% fit"
                        ):
                            col_a, col_b, col_c = st.columns(3)
                            with col_a:
                                st.metric("Fit Score", f"{score}%")
                            with col_b:
                                st.metric("Recommendation", recommendation)
                            with col_c:
                                st.metric("Location", job.get("job_city", location))

                            st.info(f"💡 {job.get('fit_summary', '')}")

                            col_d, col_e = st.columns(2)
                            with col_d:
                                st.markdown("**✅ Your Matching Skills**")
                                for s in job.get("top_matching_skills", []):
                                    st.write(f"• {s}")
                            with col_e:
                                st.markdown("**📋 Key Requirements**")
                                for r in job.get("key_requirements", []):
                                    st.write(f"• {r}")

                            st.markdown("**💰 Salary Estimate**")
                            st.write(job.get("salary_estimate", "Not specified"))

                            st.markdown("**🗣️ Your One-Line Pitch**")
                            st.success(job.get("one_line_pitch", ""))

                            # Apply link
                            apply_url = job.get("job_apply_link", "")
                            if apply_url:
                                st.link_button("🔗 Apply Now", apply_url)
                            else:
                                job_url = job.get("job_google_link", "")
                                if job_url:
                                    st.link_button("🔗 View Job", job_url)

                    # Summary table
                    st.divider()
                    st.subheader("📊 Quick Summary Table")
                    summary_data = []
                    for job in filtered:
                        summary_data.append({
                            "Role": job.get("job_title", ""),
                            "Company": job.get("employer_name", ""),
                            "Fit Score": f"{job.get('fit_score', 0)}%",
                            "Recommendation": job.get("apply_recommendation", ""),
                            "Salary": job.get("salary_estimate", "")
                        })
                    st.dataframe(summary_data, use_container_width=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption("Built by Meghana · Day 85 of 90 · AI Job Search Agent · Groq + JSearch + Streamlit")