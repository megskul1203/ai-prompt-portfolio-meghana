import streamlit as st
import os
import json
import re
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "openai/gpt-oss-120b"

# ── Meghana's profile ─────────────────────────────────────────────────────────
MEGHANA_PROFILE = """
Name: Meghana S Kulkarni
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
def call_ai(prompt: str, system: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user",   "content": prompt}
        ],
        temperature=0.7,
        max_tokens=2000
    )
    return response.choices[0].message.content

def extract_json(text: str):
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        return json.loads(match.group())
    return json.loads(text)

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Cold Email Generator",
    page_icon="📧",
    layout="wide"
)

st.title("📧 AI Cold Email Generator")
st.caption("Company + role → personalised cold email to the hiring manager")
st.divider()

# ── Inputs ────────────────────────────────────────────────────────────────────
col1, col2 = st.columns(2)
with col1:
    company = st.text_input(
        "Company Name",
        placeholder="e.g. Freshworks, QpiAI, upGrad, Postman..."
    )
    role = st.selectbox(
        "Role you're targeting",
        [
            "AI Technical Writer",
            "Prompt Engineer",
            "AI Curriculum Designer",
            "AI Content Specialist",
            "Technical Writer",
            "AI Learning Experience Designer",
            "LLM Trainer / AI Trainer"
        ]
    )
with col2:
    hiring_manager = st.text_input(
        "Hiring Manager Name (optional)",
        placeholder="e.g. Priya Sharma — leave blank if unknown"
    )
    company_context = st.text_area(
        "What do you know about this company? (optional)",
        height=100,
        placeholder="e.g. Freshworks builds CRM software for SMBs, recently launched Freddy AI their LLM assistant..."
    )

tone = st.radio(
    "Email tone",
    ["Professional & Confident", "Conversational & Warm", "Ultra-short (5 lines max)"],
    horizontal=True
)

generate_btn = st.button("📧 Generate Cold Email", type="primary")

# ── Generation ────────────────────────────────────────────────────────────────
if generate_btn:
    if not company.strip():
        st.warning("Please enter a company name.")
    else:
        with st.spinner(f"Writing your cold email to {company}..."):

            manager_line = f"Hiring Manager Name: {hiring_manager}" if hiring_manager.strip() else "Hiring Manager Name: Unknown — use a professional generic opening"
            context_line = f"Company Context: {company_context}" if company_context.strip() else "Company Context: Not provided — infer from company name and role"

            tone_guide = {
                "Professional & Confident": "Formal, confident, direct. Short paragraphs. No fluff. Reads like it came from someone who knows their worth.",
                "Conversational & Warm": "Friendly but professional. Feels like a human wrote it, not a template. Slightly informal but still respectful.",
                "Ultra-short (5 lines max)": "Maximum 5 lines. Subject line + 3-4 sentence email. Every word earns its place. No filler."
            }

            prompt = f"""
You are an expert career coach helping Meghana write a cold email to a hiring manager.

Meghana's Profile:
{MEGHANA_PROFILE}

Target Details:
Company: {company}
Role: {role}
{manager_line}
{context_line}
Tone: {tone} — {tone_guide[tone]}

Write a cold email that:
1. References specific projects from Meghana's portfolio that are relevant to THIS company and role
2. Shows she understands what the company does
3. Is NOT a cover letter — it's a direct human outreach
4. Has a clear, specific ask (15-minute call or reply)
5. Includes the portfolio link naturally

Respond ONLY with valid JSON. No extra text. Format:
{{
  "subject_line": "the email subject line",
  "email_body": "the full email body with proper line breaks using \\n",
  "why_it_works": ["reason 1 why this email will get a response", "reason 2", "reason 3"],
  "personalisation_used": ["specific detail 1 that makes this not a template", "detail 2"],
  "follow_up_tip": "one specific tip for following up if no response in 5 days",
  "best_send_time": "best day and time to send this email for highest open rate",
  "linkedin_connect_note": "a 1-line LinkedIn connection note to send alongside the email"
}}
"""
            raw = call_ai(prompt, "You are an expert career coach and cold email specialist.")

        try:
            data = extract_json(raw)

            # ── Subject Line ──────────────────────────────────────────────────
            st.subheader("📧 Your Cold Email")
            st.markdown("**Subject Line:**")
            subject = data.get("subject_line", "")
            st.code(subject, language=None)

            # ── Email Body ────────────────────────────────────────────────────
            st.markdown("**Email Body:**")
            email_body = data.get("email_body", "")
            st.text_area(
                label="email",
                value=email_body,
                height=320,
                label_visibility="collapsed"
            )

            # ── Copy buttons ──────────────────────────────────────────────────
            col3, col4 = st.columns(2)
            with col3:
                st.download_button(
                    "⬇️ Download Email (.txt)",
                    data=f"Subject: {subject}\n\n{email_body}",
                    file_name=f"cold_email_{company.replace(' ', '_')}.txt",
                    mime="text/plain"
                )
            with col4:
                st.download_button(
                    "⬇️ Download Full Analysis (.json)",
                    data=json.dumps(data, indent=2),
                    file_name=f"email_analysis_{company.replace(' ', '_')}.json",
                    mime="application/json"
                )

            st.divider()

            # ── Why it works ──────────────────────────────────────────────────
            col5, col6 = st.columns(2)
            with col5:
                st.subheader("✅ Why This Email Works")
                for reason in data.get("why_it_works", []):
                    st.success(f"• {reason}")

                st.subheader("🎯 Personalisation Used")
                for detail in data.get("personalisation_used", []):
                    st.info(f"• {detail}")

            with col6:
                st.subheader("📬 Send Strategy")
                st.markdown("**Best time to send:**")
                st.write(data.get("best_send_time", ""))

                st.markdown("**Follow-up tip:**")
                st.warning(data.get("follow_up_tip", ""))

                st.markdown("**LinkedIn connection note:**")
                linkedin_note = data.get("linkedin_connect_note", "")
                st.text_area(
                    label="linkedin",
                    value=linkedin_note,
                    height=80,
                    label_visibility="collapsed"
                )
                st.download_button(
                    "⬇️ Copy LinkedIn Note",
                    data=linkedin_note,
                    file_name="linkedin_note.txt",
                    mime="text/plain"
                )

        except Exception as e:
            st.error(f"Could not parse AI response. Please try again. ({e})")
            with st.expander("Raw AI response"):
                st.text(raw)

# ── Target companies quick launch ─────────────────────────────────────────────
st.divider()
st.subheader("🎯 Your Target Companies")
st.caption("Click any to pre-fill the company name above")

targets = [
    ("Freshworks", "AI Technical Writer"),
    ("QpiAI", "AI Technical Writer"),
    ("Postman", "AI Technical Writer"),
    ("upGrad", "AI Curriculum Designer"),
    ("Scaler", "AI Curriculum Designer"),
    ("Sprinklr", "Prompt Engineer"),
    ("Yellow.ai", "Prompt Engineer"),
    ("Observe.AI", "Prompt Engineer"),
    ("Sarvam AI", "Prompt Engineer"),
    ("Chargebee", "AI Technical Writer"),
]

cols = st.columns(5)
for i, (co, ro) in enumerate(targets):
    with cols[i % 5]:
        if st.button(f"{co}", key=f"target_{co}"):
            st.info(f"Type **{co}** in the Company Name field above and select **{ro}** as the role, then click Generate.")

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption("Built by Meghana · Day 89 of 90 · AI Cold Email Generator · Groq + Streamlit")