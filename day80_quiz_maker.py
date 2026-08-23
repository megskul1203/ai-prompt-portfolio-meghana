import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

st.set_page_config(
    page_title="AI Quiz Maker",
    page_icon="🧩",
    layout="centered"
)

st.title("🧩 AI Quiz Maker")
st.markdown("Paste any training content and generate a ready-to-use quiz instantly.")

@st.cache_resource
def load_client():
    return Groq(api_key=os.getenv("GROQ_API_KEY"))

client = load_client()

def generate_quiz(content, num_questions, difficulty, topic):
    prompt = f"""You are an expert instructional designer creating a quiz.

Based on the following training content, generate exactly {num_questions} multiple choice questions.

Training Content:
{content}

Requirements:
- Difficulty level: {difficulty}
- Topic/Subject: {topic}
- Each question must have exactly 4 options (A, B, C, D)
- Only one option is correct
- Questions should test real understanding, not just memory
- For harder difficulty, include application and analysis questions

Respond with ONLY a valid JSON array. No explanation, no markdown, no extra text.
Format exactly like this:
[
  {{
    "question": "Question text here?",
    "options": {{
      "A": "First option",
      "B": "Second option", 
      "C": "Third option",
      "D": "Fourth option"
    }},
    "correct": "A",
    "explanation": "Brief explanation of why this is correct"
  }}
]"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# ── UI ────────────────────────────────────────────────────────
topic = st.text_input("📌 Topic or Subject", placeholder="e.g. Prompt Engineering, Python Basics, Company Policy")

content = st.text_area(
    "📄 Paste Your Training Content Here",
    height=200,
    placeholder="Paste any training material, document excerpt, or topic notes here..."
)

col1, col2 = st.columns(2)
with col1:
    num_questions = st.selectbox("🔢 Number of Questions", [3, 5, 8, 10])
with col2:
    difficulty = st.selectbox("📊 Difficulty Level", ["Beginner", "Intermediate", "Advanced"])

if st.button("🎯 Generate Quiz") and content.strip() and topic.strip():
    with st.spinner("Creating your quiz..."):
        raw = generate_quiz(content, num_questions, difficulty, topic)

    try:
        # Clean response in case of any markdown wrapping
        clean = raw.strip()
        if clean.startswith("```"):
            clean = clean.split("```")[1]
            if clean.startswith("json"):
                clean = clean[4:]
        clean = clean.strip()

        questions = json.loads(clean)

        st.markdown("---")
        st.markdown("## 📋 Your Quiz")

        # Display questions
        for i, q in enumerate(questions, 1):
            st.markdown(f"**Question {i}:** {q['question']}")
            for key, value in q['options'].items():
                st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;{key}) {value}")
            
            with st.expander(f"See Answer for Q{i}"):
                st.success(f"✅ Correct Answer: {q['correct']}) {q['options'][q['correct']]}")
                st.info(f"💡 {q['explanation']}")
            
            st.markdown("")

        # Download as text
        quiz_text = f"QUIZ: {topic}\nDifficulty: {difficulty}\n\n"
        for i, q in enumerate(questions, 1):
            quiz_text += f"Q{i}. {q['question']}\n"
            for key, value in q['options'].items():
                quiz_text += f"   {key}) {value}\n"
            quiz_text += f"Answer: {q['correct']}\n"
            quiz_text += f"Explanation: {q['explanation']}\n\n"

        st.download_button(
            label="⬇️ Download Quiz",
            data=quiz_text,
            file_name=f"{topic.replace(' ', '_')}_quiz.txt",
            mime="text/plain"
        )

    except json.JSONDecodeError:
        st.error("The AI returned an unexpected format. Please try again.")
        st.code(raw)

st.markdown("---")
st.caption("Built by Meghana · Day 80 · AI Quiz Maker")