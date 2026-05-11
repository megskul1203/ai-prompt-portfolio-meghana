import streamlit as st
import os
import json
import re
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "llama-3.3-70b-versatile"

# ── Meghana's background — edit this anytime ──────────────────────────────────
MEGHANA_PROFILE = """
Name: Meghana
Current Role: Content Developer in L&D (Learning & Development)
Education: Computer Science Engineering degree
Experience:
- 3 years UPSC preparation (research, writing, structured thinking)
- Promoted from Content Writer to Content Developer
- 84 days of dedicated AI study

Technical Skills Built:
- Python (functions, APIs, JSON, file handling)
- Groq API integration (LLaMA 3.3 70B model)
- RAG Pipeline (ChromaDB + sentence-transformers + Groq)
- Streamlit (6 deployed web applications)
- Prompt Engineering (zero-shot, few-shot, chain-of-thought, role prompting)
- Embeddings and semantic search (all-MiniLM-L6-v2)
- Vector databases (ChromaDB)
- AI evaluation metrics (Faithfulness, Answer Relevancy, Context Precision)

Deployed Applications:
1. RAG Pipeline — meghana-rag-pipeline.streamlit.app
2. AI Course Generator — meghana-course-generator.streamlit.app
3. AI Quiz Maker — meghana-quiz-maker.streamlit.app
4. AI Prompt Improver — meghana-prompt-improver.streamlit.app
5. AI Flashcard Generator — meghana-flashcard-generator.streamlit.app
6. Combined L&D Toolkit — (Day 83, deployed)

Soft Skills:
- Instructional design and curriculum development
- Technical writing and content development
- Structured learning design using Bloom's Taxonomy
- Research and synthesis (from UPSC preparation)
- Self-directed learning (84-day AI journey with zero mentor)

Target Roles: AI Technical Writer, Prompt Engineer, AI Curriculum Designer
"""

# ── Helpers ───────────────────────────────────────────────────────────────────
def call_ai(prompt: str, system: str = "You are an expert career coach and hiring specialist.") -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user",   "content": prompt}
        ],
        temperature=0.5,
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
    page_title="JD Analyser — Meghana",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 AI Job Description Analyser")
st.caption("Paste any JD → get skill gap analysis, strength mapping, and a tailored pitch")
st.divider()

# ── Input ─────────────────────────────────────────────────────────────────────
jd_text = st.text_area(
    "Paste the full Job Description here",
    height=280,
    placeholder="Copy and paste the entire job description — title, responsibilities, requirements, everything..."
)

role_type = st.selectbox(
    "Which role category is this closest to?",
    [
        "AI Technical Writer",
        "Prompt Engineer",
        "AI Curriculum Designer",
        "AI Learning Experience Designer",
        "Other"
    ]
)

analyse_btn = st.button("🔍 Analyse This JD", type="primary")

# ── Analysis ──────────────────────────────────────────────────────────────────
if analyse_btn:
    if not jd_text.strip():
        st.warning("Please paste a job description first.")
    else:
        with st.spinner("Analysing JD and mapping to your profile..."):

            prompt = f"""
You are an expert career coach helping a candidate called Meghana apply for a {role_type} role.

Here is Meghana's full profile:
{MEGHANA_PROFILE}

Here is the Job Description she is applying to:
{jd_text}

Analyse the JD against Meghana's profile and respond ONLY with valid JSON. No extra text. Format:

{{
  "role_title": "extracted job title from JD",
  "company_name": "extracted company name if visible, else Unknown",
  "required_skills": {{
    "technical": ["skill1", "skill2", "skill3"],
    "soft": ["skill1", "skill2", "skill3"]
  }},
  "gap_analysis": {{
    "strong_match": ["skills where Meghana is clearly strong"],
    "developing": ["skills Meghana is actively building"],
    "gaps": ["skills Meghana does not yet have"]
  }},
  "meghana_strengths": [
    "specific strength 1 that matches this JD",
    "specific strength 2 that matches this JD",
    "specific strength 3 that matches this JD",
    "specific strength 4 that matches this JD"
  ],
  "tailored_pitch": "A 3-4 sentence paragraph Meghana can use as her cover letter opening or interview introduction. It should reference her 84-day AI journey, her 6 deployed apps, her L&D background, and connect directly to this specific role.",
  "interview_questions": [
    {{
      "question": "likely interview question 1 for this role",
      "answer_hint": "what Meghana should talk about from her background"
    }},
    {{
      "question": "likely interview question 2 for this role",
      "answer_hint": "what Meghana should talk about from her background"
    }},
    {{
      "question": "likely interview question 3 for this role",
      "answer_hint": "what Meghana should talk about from her background"
    }},
    {{
      "question": "likely interview question 4 for this role",
      "answer_hint": "what Meghana should talk about from her background"
    }},
    {{
      "question": "likely interview question 5 for this role",
      "answer_hint": "what Meghana should talk about from her background"
    }}
  ],
  "fit_score": {{
    "score": 75,
    "summary": "one sentence explaining the score"
  }}
}}
"""
            raw = call_ai(prompt)

        try:
            data = extract_json(raw)

            # ── Header ────────────────────────────────────────────────────────
            col_title, col_score = st.columns([3, 1])
            with col_title:
                st.subheader(f"📋 {data.get('role_title', 'Role')} @ {data.get('company_name', 'Company')}")
            with col_score:
                score = data.get("fit_score", {}).get("score", 0)
                color = "green" if score >= 70 else "orange" if score >= 50 else "red"
                st.metric("Fit Score", f"{score}%")
                st.caption(data.get("fit_score", {}).get("summary", ""))

            st.divider()

            # ── Required Skills ───────────────────────────────────────────────
            st.subheader("🎯 What This Role Needs")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Technical Skills**")
                for s in data.get("required_skills", {}).get("technical", []):
                    st.write(f"• {s}")
            with col2:
                st.markdown("**Soft Skills**")
                for s in data.get("required_skills", {}).get("soft", []):
                    st.write(f"• {s}")

            st.divider()

            # ── Gap Analysis ──────────────────────────────────────────────────
            st.subheader("📊 Your Gap Analysis")
            col3, col4, col5 = st.columns(3)
            with col3:
                st.success("✅ Strong Match")
                for s in data.get("gap_analysis", {}).get("strong_match", []):
                    st.write(f"• {s}")
            with col4:
                st.warning("🔨 Actively Building")
                for s in data.get("gap_analysis", {}).get("developing", []):
                    st.write(f"• {s}")
            with col5:
                st.error("❌ Gaps to Address")
                gaps = data.get("gap_analysis", {}).get("gaps", [])
                if gaps:
                    for s in gaps:
                        st.write(f"• {s}")
                else:
                    st.write("No major gaps identified!")

            st.divider()

            # ── Strengths ─────────────────────────────────────────────────────
            st.subheader("💪 Your Specific Strengths for This Role")
            for strength in data.get("meghana_strengths", []):
                st.info(f"⭐ {strength}")

            st.divider()

            # ── Tailored Pitch ────────────────────────────────────────────────
            st.subheader("🗣️ Your Tailored Pitch")
            st.caption("Use this as your cover letter opening or interview introduction")
            pitch = data.get("tailored_pitch", "")
            st.success(pitch)
            st.download_button(
                "⬇️ Copy Pitch as .txt",
                data=pitch,
                file_name=f"pitch_{data.get('company_name', 'company').replace(' ', '_')}.txt",
                mime="text/plain",
                key="pitch_download"
            )

            st.divider()

            # ── Interview Prep ────────────────────────────────────────────────
            st.subheader("📝 Likely Interview Questions")
            for i, item in enumerate(data.get("interview_questions", []), 1):
                with st.expander(f"Q{i}: {item['question']}"):
                    st.markdown(f"**💡 Talk about:** {item['answer_hint']}")

            st.divider()

            # ── Full JSON download ────────────────────────────────────────────
            st.download_button(
                "⬇️ Download Full Analysis (JSON)",
                data=json.dumps(data, indent=2),
                file_name="jd_analysis.json",
                mime="application/json",
                key="full_download"
            )

        except Exception as e:
            st.error(f"Could not parse the AI response. Please try again. ({e})")
            with st.expander("Raw AI response (for debugging)"):
                st.text(raw)

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption("Built by Meghana · Day 84 of 90 · AI Job Description Analyser · Groq + Streamlit")