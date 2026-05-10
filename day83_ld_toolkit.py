import streamlit as st
import os
import json
import re
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "llama-3.3-70b-versatile"

# ── Shared helper ──────────────────────────────────────────────────────────────
def call_ai(prompt: str, system: str = "You are an expert L&D specialist.") -> str:
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
    """Pull the first JSON block out of an AI response, even if it has extra text."""
    match = re.search(r'\{.*\}|\[.*\]', text, re.DOTALL)
    if match:
        return json.loads(match.group())
    return json.loads(text)          # last-resort attempt

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Meghana's L&D Toolkit",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Meghana's AI-Powered L&D Toolkit")
st.caption("Course Generator · Quiz Maker · Flashcard Generator · Prompt Improver")
st.divider()

tab1, tab2, tab3, tab4 = st.tabs([
    "📚 Course Generator",
    "🧩 Quiz Maker",
    "🃏 Flashcard Generator",
    "✨ Prompt Improver"
])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — COURSE GENERATOR
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
    st.header("📚 AI Course Content Generator")
    st.write("Enter a topic and get a complete, structured course outline instantly.")

    col1, col2 = st.columns(2)
    with col1:
        topic    = st.text_input("Course Topic", placeholder="e.g. Effective Business Communication", key="cg_topic")
        audience = st.selectbox("Target Audience", ["Freshers", "Mid-level Professionals", "Senior Leaders", "Mixed"], key="cg_audience")
    with col2:
        duration   = st.selectbox("Course Duration", ["30 minutes", "1 hour", "2 hours", "Half day", "Full day"], key="cg_duration")
        difficulty = st.selectbox("Difficulty Level", ["Beginner", "Intermediate", "Advanced"], key="cg_diff")

    if st.button("🚀 Generate Course Outline", key="cg_btn"):
        if not topic.strip():
            st.warning("Please enter a course topic.")
        else:
            with st.spinner("Building your course outline..."):
                prompt = f"""
Create a complete course outline for:
- Topic: {topic}
- Audience: {audience}
- Duration: {duration}
- Difficulty: {difficulty}

Use Bloom's Taxonomy action verbs for learning objectives.
Structure your response with clear sections:
1. Course Overview (2-3 sentences)
2. Learning Objectives (4-5 bullet points using Bloom's verbs)
3. Course Modules (3-5 modules, each with title, duration, and 3 key topics)
4. Assessment Strategy (how learners will be evaluated)
5. Facilitator Notes (2-3 delivery tips)
"""
                result = call_ai(prompt)

            st.success("Course outline generated!")
            st.markdown(result)
            st.download_button(
                "⬇️ Download Course Outline",
                data=result,
                file_name=f"course_{topic.replace(' ', '_')}.txt",
                mime="text/plain",
                key="cg_download"
            )

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — QUIZ MAKER
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.header("🧩 AI Quiz Maker")
    st.write("Paste any training content and generate MCQ questions with answers and explanations.")

    content_quiz = st.text_area(
        "Paste your training content here",
        height=180,
        placeholder="Paste a paragraph, module text, or topic description...",
        key="qm_content"
    )
    col3, col4 = st.columns(2)
    with col3:
        num_questions = st.slider("Number of Questions", 3, 10, 5, key="qm_num")
    with col4:
        quiz_diff = st.selectbox("Difficulty", ["Beginner", "Intermediate", "Advanced", "Mixed"], key="qm_diff")

    if st.button("🧩 Generate Quiz", key="qm_btn"):
        if not content_quiz.strip():
            st.warning("Please paste some training content.")
        else:
            with st.spinner("Generating quiz questions..."):
                prompt = f"""
You are an expert instructional designer. Generate {num_questions} MCQ questions from the content below.
Difficulty level: {quiz_diff}

Content:
{content_quiz}

Respond ONLY with a valid JSON array. No extra text. Format:
[
  {{
    "question": "question text here",
    "options": {{
      "A": "option text",
      "B": "option text",
      "C": "option text",
      "D": "option text"
    }},
    "correct_answer": "A",
    "explanation": "why this answer is correct"
  }}
]
"""
                raw = call_ai(prompt)

            try:
                questions = extract_json(raw)
                st.success(f"Generated {len(questions)} questions!")

                for i, q in enumerate(questions, 1):
                    with st.expander(f"Q{i}: {q['question']}"):
                        for letter, option_text in q["options"].items():
                            st.write(f"**{letter}.** {option_text}")
                        st.success(f"✅ Correct Answer: {q['correct_answer']}")
                        st.info(f"💡 Explanation: {q['explanation']}")

                st.download_button(
                    "⬇️ Download Quiz (JSON)",
                    data=json.dumps(questions, indent=2),
                    file_name="quiz.json",
                    mime="application/json",
                    key="qm_download"
                )
            except Exception as e:
                st.error(f"Could not parse AI response. Try again. ({e})")
                with st.expander("Raw AI response"):
                    st.text(raw)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 — FLASHCARD GENERATOR
# ══════════════════════════════════════════════════════════════════════════════
with tab3:
    st.header("🃏 AI Flashcard Generator")
    st.write("Turn any training content into active recall flashcards.")

    content_flash = st.text_area(
        "Paste your training content here",
        height=180,
        placeholder="Paste a paragraph, module text, or topic description...",
        key="fc_content"
    )
    col5, col6 = st.columns(2)
    with col5:
        num_cards  = st.slider("Number of Flashcards", 3, 15, 6, key="fc_num")
    with col6:
        card_diff  = st.selectbox("Difficulty Level", ["Beginner", "Intermediate", "Advanced", "Mixed"], key="fc_diff")

    if st.button("🃏 Generate Flashcards", key="fc_btn"):
        if not content_flash.strip():
            st.warning("Please paste some training content.")
        else:
            with st.spinner("Creating your flashcards..."):
                diff_guide = {
                    "Beginner":     "Focus on definitions and key terms.",
                    "Intermediate": "Focus on how and why things work.",
                    "Advanced":     "Focus on application, edge cases, and nuances.",
                    "Mixed":        "Mix definitions, how/why, and application questions."
                }
                prompt = f"""
Create {num_cards} flashcards from the content below.
Difficulty: {card_diff} — {diff_guide[card_diff]}

Content:
{content_flash}

Respond ONLY with a valid JSON array. No extra text. Format:
[
  {{
    "question": "question for front of card",
    "answer": "concise answer for back of card",
    "difficulty": "{card_diff}"
  }}
]
"""
                raw = call_ai(prompt)

            try:
                cards = extract_json(raw)
                st.success(f"Generated {len(cards)} flashcards!")

                # Interactive flip-style display
                if "fc_index" not in st.session_state:
                    st.session_state.fc_index = 0
                if "fc_show_answer" not in st.session_state:
                    st.session_state.fc_show_answer = False
                if "fc_cards" not in st.session_state:
                    st.session_state.fc_cards = []

                st.session_state.fc_cards = cards
                st.session_state.fc_index = 0
                st.session_state.fc_show_answer = False

                card = cards[st.session_state.fc_index]
                total = len(cards)
                idx   = st.session_state.fc_index

                st.markdown(f"**Card {idx + 1} of {total}** — {card.get('difficulty', card_diff)}")
                st.info(f"❓ **{card['question']}**")

                col7, col8, col9 = st.columns(3)
                with col7:
                    if st.button("⬅️ Previous", key="fc_prev") and idx > 0:
                        st.session_state.fc_index -= 1
                        st.session_state.fc_show_answer = False
                        st.rerun()
                with col8:
                    if st.button("👁️ Reveal Answer", key="fc_reveal"):
                        st.session_state.fc_show_answer = True
                        st.rerun()
                with col9:
                    if st.button("➡️ Next", key="fc_next") and idx < total - 1:
                        st.session_state.fc_index += 1
                        st.session_state.fc_show_answer = False
                        st.rerun()

                if st.session_state.fc_show_answer:
                    st.success(f"✅ **{card['answer']}**")

                st.divider()
                st.markdown("**All Flashcards**")
                for j, c in enumerate(cards, 1):
                    with st.expander(f"Card {j}: {c['question']}"):
                        st.write(c["answer"])

                st.download_button(
                    "⬇️ Download Flashcards (JSON)",
                    data=json.dumps(cards, indent=2),
                    file_name="flashcards.json",
                    mime="application/json",
                    key="fc_download"
                )
            except Exception as e:
                st.error(f"Could not parse response. Try again. ({e})")
                with st.expander("Raw AI response"):
                    st.text(raw)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 4 — PROMPT IMPROVER
# ══════════════════════════════════════════════════════════════════════════════
with tab4:
    st.header("✨ AI Prompt Improver")
    st.write("Paste any weak prompt and get a stronger, more effective version with explanation.")

    weak_prompt = st.text_area(
        "Your original prompt",
        height=150,
        placeholder="e.g. Write something about leadership for my team.",
        key="pi_prompt"
    )
    use_case = st.selectbox(
        "What is this prompt for?",
        ["L&D / Training content", "Quiz or assessment", "Email or communication",
         "Research or analysis", "Creative writing", "General use"],
        key="pi_usecase"
    )

    if st.button("✨ Improve My Prompt", key="pi_btn"):
        if not weak_prompt.strip():
            st.warning("Please enter a prompt to improve.")
        else:
            with st.spinner("Analysing and improving your prompt..."):
                prompt = f"""
You are an expert prompt engineer specialising in {use_case}.

Analyse this prompt and improve it:
"{weak_prompt}"

Respond ONLY with valid JSON. No extra text. Format:
{{
  "original_prompt": "the original prompt",
  "problems_identified": ["problem 1", "problem 2", "problem 3"],
  "improved_prompt": "your rewritten, stronger version of the prompt",
  "changes_made": ["change 1", "change 2", "change 3"],
  "techniques_used": ["technique name 1", "technique name 2"]
}}
"""
                raw = call_ai(prompt)

            try:
                result = extract_json(raw)

                st.subheader("🔍 Problems Identified")
                for p in result.get("problems_identified", []):
                    st.warning(f"⚠️ {p}")

                st.subheader("✅ Improved Prompt")
                st.success(result.get("improved_prompt", ""))

                col10, col11 = st.columns(2)
                with col10:
                    st.subheader("🔧 Changes Made")
                    for c in result.get("changes_made", []):
                        st.write(f"• {c}")
                with col11:
                    st.subheader("🎯 Techniques Used")
                    for t in result.get("techniques_used", []):
                        st.markdown(f"`{t}`")

                st.download_button(
                    "⬇️ Download Analysis (JSON)",
                    data=json.dumps(result, indent=2),
                    file_name="prompt_analysis.json",
                    mime="application/json",
                    key="pi_download"
                )
            except Exception as e:
                st.error(f"Could not parse response. Try again. ({e})")
                with st.expander("Raw AI response"):
                    st.text(raw)

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption("Built by Meghana · Day 83 of 90 · AI-Powered L&D Toolkit · Groq + Streamlit")