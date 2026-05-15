import streamlit as st
import os
import json
import re
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "llama-3.3-70b-versatile"

# ── Meghana's profile ─────────────────────────────────────────────────────────
MEGHANA_PROFILE = """
Name: Meghana S Kulkarni
Current Role: Content Developer at Bigbasket (promoted from Content Writer in 13 months)
Education: B.E. Computer Science Engineering, PDA College of Engineering, 2020
Location: Bengaluru, India
Email: megskul1203@gmail.com
Phone: +91 7022102233
GitHub: github.com/megskul1203
LinkedIn: linkedin.com/in/meghana-kulkarni-2a4538317
Portfolio: megskul1203.github.io/ai-prompt-portfolio-meghana

AI Journey:
- 90 days of self-directed AI study (no bootcamp, no mentor)
- 10 live deployed Streamlit applications

Key Projects:
1. RAG Pipeline — full retrieval-augmented generation with ChromaDB + semantic search
2. AI Course Generator — Bloom's Taxonomy based curriculum generation
3. AI Quiz Maker — training content to MCQ with JSON structured outputs
4. AI Prompt Improver — analyses and rewrites weak prompts with technique explanations
5. AI Flashcard Generator — active recall cards at multiple difficulty levels
6. Combined L&D Toolkit — 4 tools in one multi-tab app
7. AI Job Description Analyser — JD to fit score, gap analysis, tailored pitch
8. AI Job Search Agent — live jobs from LinkedIn/Indeed ranked by profile fit
9. AI Learning Path Generator — Bloom's Taxonomy week-by-week learning plans
10. AI Cold Email Generator — personalised outreach emails for job applications

Technical Skills:
Python, Groq API, LLaMA 3.3 70B, RAG Pipelines, ChromaDB, Streamlit,
Prompt Engineering, REST APIs, RapidAPI, sentence-transformers, JSON parsing

L&D Skills:
Instructional Design, Bloom's Taxonomy, eLearning scripting, Articulate,
Vyond, Stepping Stone LMS, Technical Writing, Storyboarding

Target Roles: AI Technical Writer, Prompt Engineer, AI Curriculum Designer
Salary Target: 12-18 LPA
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