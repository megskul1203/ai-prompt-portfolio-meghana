import streamlit as st
import os
import json
import re
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "llama-3.3-70b-versatile"

# ── Meghana's profile context ─────────────────────────────────────────────────
MEGHANA_PROFILE = """
Name: Meghana S Kulkarni
Current Role: Content Developer at Bigbasket (promoted from Content Writer in 13 months)
Education: B.E. Computer Science Engineering, PDA College of Engineering, 2020
Location: Bengaluru, India
Portfolio: megskul1203.github.io/ai-prompt-portfolio-meghana
GitHub: github.com/megskul1203

90-day AI Journey — 10 live deployed applications:
1. RAG Pipeline — ChromaDB + semantic search + hallucination prevention
2. AI Course Generator — Bloom's Taxonomy based curriculum generation
3. AI Quiz Maker — MCQ generation with JSON structured outputs
4. AI Prompt Improver — prompt analysis and rewriting with technique explanations
5. AI Flashcard Generator — active recall cards at multiple difficulty levels
6. Combined L&D Toolkit — 4 tools in one multi-tab Streamlit app
7. AI Job Description Analyser — fit score, gap analysis, tailored pitch
8. AI Job Search Agent — live jobs from LinkedIn/Indeed ranked by profile fit
9. AI Learning Path Generator — Bloom's Taxonomy week-by-week learning plans
10. AI Cold Email Generator — personalised outreach emails for job applications

Technical Skills: Python, Groq API, LLaMA 3.3 70B, RAG Pipelines, ChromaDB,
Streamlit, Prompt Engineering, REST APIs, RapidAPI, sentence-transformers

L&D Skills: Instructional Design, Bloom's Taxonomy, eLearning scripting,
Articulate, Vyond, Stepping Stone LMS, Technical Writing, Storyboarding

Target Roles: AI Technical Writer, Prompt Engineer, AI Curriculum Designer
"""

# ── Pre-loaded questions by role ──────────────────────────────────────────────
QUESTION_BANK = {
    "AI Technical Writer": [
        "Tell me about yourself and why you're applying for this role.",
        "How would you document a complex AI feature for a non-technical audience?",
        "Walk me through how you would approach documenting an API.",
        "How do you stay current with AI and technology trends?",
        "Can you explain RAG in simple terms as if writing for a developer audience?",
        "What's the difference between a user guide and a technical reference document?",
        "How would you handle a situation where the engineer explains something you don't understand?",
        "Describe a time you had to simplify a complex technical concept."
    ],
    "Prompt Engineer": [
        "Tell me about yourself and why you're applying for this role.",
        "What is prompt engineering and why does it matter?",
        "Explain the difference between zero-shot, few-shot, and chain-of-thought prompting.",
        "How would you evaluate whether a prompt is performing well?",
        "Walk me through how you built your RAG pipeline.",
        "What is hallucination in LLMs and how do you prevent it?",
        "How would you design a prompt for a customer support chatbot?",
        "What metrics would you use to measure LLM output quality?"
    ],
    "AI Curriculum Designer": [
        "Tell me about yourself and why you're applying for this role.",
        "How does Bloom's Taxonomy apply to AI-powered learning design?",
        "How would you use AI to personalise learning paths for different learners?",
        "Walk me through one of your AI L&D tools and how it was designed.",
        "What's the difference between instructional design and content writing?",
        "How would you measure the effectiveness of an AI-generated course?",
        "How do you balance AI automation with human instructional design expertise?",
        "Describe your experience with eLearning authoring tools."
    ],
    "General / HR Round": [
        "Tell me about yourself.",
        "Why are you switching from content development to AI roles?",
        "Where do you see yourself in 3 years?",
        "What is your biggest strength and weakness?",
        "Why should we hire you over other candidates?",
        "How do you handle learning something completely new?",
        "Tell me about a time you took initiative without being asked.",
        "What salary are you expecting?"
    ]
}

# ── Helpers ───────────────────────────────────────────────────────────────────
def call_ai(prompt: str, system: str) -> str:
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
    page_title="AI Interview Answer Coach",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 AI Interview Answer Coach")
st.caption("Enter any interview question + your draft answer → get scored feedback and an improved version")
st.divider()

# ── Mode selector ─────────────────────────────────────────────────────────────
mode = st.radio(
    "How do you want to practice?",
    ["📋 Pick from question bank", "✍️ Enter my own question"],
    horizontal=True
)

st.divider()

# ── Question input ────────────────────────────────────────────────────────────
question = ""

if mode == "📋 Pick from question bank":
    col1, col2 = st.columns(2)
    with col1:
        role_category = st.selectbox(
            "Role category",
            list(QUESTION_BANK.keys())
        )
    with col2:
        selected_q = st.selectbox(
            "Select a question",
            QUESTION_BANK[role_category]
        )
    question = selected_q

else:
    question = st.text_input(
        "Enter the interview question",
        placeholder="e.g. How would you document an API endpoint?"
    )

# ── Answer input ──────────────────────────────────────────────────────────────
if question:
    st.markdown(f"**Question:** {question}")
    st.markdown("---")

draft_answer = st.text_area(
    "Your draft answer",
    height=200,
    placeholder="Type your answer here as you would say it in an interview. Don't overthink it — just write naturally. The coach will improve it."
)

target_role = st.selectbox(
    "Which role is this interview for?",
    ["AI Technical Writer", "Prompt Engineer",
     "AI Curriculum Designer", "General / HR Round"]
)

coach_btn = st.button("🎤 Coach My Answer", type="primary")

# ── Coaching ──────────────────────────────────────────────────────────────────
if coach_btn:
    if not question.strip():
        st.warning("Please select or enter an interview question.")
    elif not draft_answer.strip():
        st.warning("Please write your draft answer first. Even a rough attempt is fine.")
    else:
        with st.spinner("Analysing your answer..."):

            prompt = f"""
You are an expert interview coach helping Meghana prepare for {target_role} interviews.

Meghana's Background:
{MEGHANA_PROFILE}

Interview Question: {question}

Meghana's Draft Answer: {draft_answer}

Analyse her answer and respond ONLY with valid JSON. No extra text:
{{
  "scores": {{
    "clarity": 7,
    "relevance": 8,
    "confidence": 6,
    "structure": 7,
    "overall": 7
  }},
  "score_explanations": {{
    "clarity": "one sentence explaining the clarity score",
    "relevance": "one sentence explaining the relevance score",
    "confidence": "one sentence explaining the confidence score",
    "structure": "one sentence explaining the structure score"
  }},
  "what_worked": [
    "specific strength 1 in her answer",
    "specific strength 2 in her answer"
  ],
  "what_to_improve": [
    "specific gap or weakness 1",
    "specific gap or weakness 2",
    "specific gap or weakness 3"
  ],
  "weak_phrases_to_avoid": [
    "phrase from her answer that weakens it",
    "another weak phrase if present"
  ],
  "improved_answer": "A rewritten version of her answer using STAR method where applicable. Should reference her actual projects and background naturally. Should sound like Meghana — confident, specific, human. 150-200 words.",
  "power_phrases": [
    "a specific strong line she should memorise and use",
    "another strong line",
    "another strong line"
  ],
  "likely_followup": "the follow-up question the interviewer will most likely ask after this answer",
  "followup_tip": "one line on how to prepare for that follow-up"
}}
"""
            raw = call_ai(prompt, "You are an expert interview coach specialising in AI and technical roles.")

        try:
            data = extract_json(raw)

            # ── Scores ────────────────────────────────────────────────────────
            st.subheader("📊 Your Answer Score")
            scores = data.get("scores", {})
            explanations = data.get("score_explanations", {})

            col1, col2, col3, col4, col5 = st.columns(5)
            metrics = [
                (col1, "Overall", "overall", "⭐"),
                (col2, "Clarity", "clarity", "💬"),
                (col3, "Relevance", "relevance", "🎯"),
                (col4, "Confidence", "confidence", "💪"),
                (col5, "Structure", "structure", "📐"),
            ]

            for col, label, key, icon in metrics:
                with col:
                    score = scores.get(key, 0)
                    color = "green" if score >= 8 else "orange" if score >= 6 else "red"
                    st.metric(f"{icon} {label}", f"{score}/10")

            st.divider()

            # ── Score explanations ────────────────────────────────────────────
            with st.expander("📋 Score Breakdown — click to see details"):
                for dimension in ["clarity", "relevance", "confidence", "structure"]:
                    st.write(f"**{dimension.capitalize()}:** {explanations.get(dimension, '')}")

            st.divider()

            # ── What worked vs improve ────────────────────────────────────────
            col6, col7 = st.columns(2)
            with col6:
                st.subheader("✅ What Worked")
                for w in data.get("what_worked", []):
                    st.success(f"• {w}")

            with col7:
                st.subheader("⚠️ What to Improve")
                for i in data.get("what_to_improve", []):
                    st.warning(f"• {i}")

            # ── Weak phrases ──────────────────────────────────────────────────
            weak = data.get("weak_phrases_to_avoid", [])
            if weak and weak[0]:
                st.subheader("🚫 Phrases to Avoid")
                for p in weak:
                    if p:
                        st.error(f'❌ "{p}"')

            st.divider()

            # ── Improved answer ───────────────────────────────────────────────
            st.subheader("✨ Improved Answer")
            st.caption("Rewritten using STAR method — sounds like you, but stronger")
            improved = data.get("improved_answer", "")
            st.info(improved)
            st.download_button(
                "⬇️ Save Improved Answer",
                data=f"Question: {question}\n\nImproved Answer:\n{improved}",
                file_name=f"answer_{question[:30].replace(' ', '_')}.txt",
                mime="text/plain"
            )

            st.divider()

            # ── Power phrases ─────────────────────────────────────────────────
            st.subheader("💪 Power Phrases to Memorise")
            st.caption("Use these exact lines in your interview")
            for phrase in data.get("power_phrases", []):
                st.success(f'🎯 "{phrase}"')

            st.divider()

            # ── Follow up ─────────────────────────────────────────────────────
            st.subheader("🔄 Likely Follow-up Question")
            st.warning(f"❓ {data.get('likely_followup', '')}")
            st.info(f"💡 Prep tip: {data.get('followup_tip', '')}")

        except Exception as e:
            st.error(f"Could not parse AI response. Please try again. ({e})")
            with st.expander("Raw AI response"):
                st.text(raw)

# ── Practice tips sidebar ─────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🎯 How to use this")
    st.markdown("""
1. **Pick a question** from the bank or type your own
2. **Write your answer** naturally — don't overthink
3. **Click Coach My Answer**
4. **Read the improved version** out loud 3 times
5. **Try again** without looking at the improved version
6. **Repeat** until your score hits 8+
    """)
    st.divider()
    st.markdown("### 📋 Your target roles")
    st.markdown("""
- 🖊️ AI Technical Writer
- ⚙️ Prompt Engineer  
- 🎓 AI Curriculum Designer
    """)
    st.divider()
    st.markdown("### 🔗 Your portfolio")
    st.markdown("[megskul1203.github.io](https://megskul1203.github.io/ai-prompt-portfolio-meghana)")

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption("Built by Meghana · Day 90 of 90 · AI Interview Answer Coach · Groq + Streamlit")