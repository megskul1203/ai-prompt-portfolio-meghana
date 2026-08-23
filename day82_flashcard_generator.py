import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

st.set_page_config(
    page_title="AI Flashcard Generator",
    page_icon="🃏",
    layout="centered"
)

st.title("🃏 AI Flashcard Generator")
st.markdown("Paste any training content and generate ready-to-use flashcards instantly.")

@st.cache_resource
def load_client():
    return Groq(api_key=os.getenv("GROQ_API_KEY"))

client = load_client()

def generate_flashcards(content, num_cards, difficulty):
    prompt = f"""You are an expert instructional designer creating flashcards 
for active recall learning.

Based on the following content, generate exactly {num_cards} flashcards.
Difficulty level: {difficulty}

Content:
{content}

Rules:
- Each flashcard must have a clear, specific question and a concise answer
- Questions should promote active recall, not just recognition
- For Beginner: focus on definitions and basic concepts
- For Intermediate: focus on how and why questions
- For Advanced: focus on application, comparison, and analysis

Respond with ONLY a valid JSON array. No explanation, no markdown, no extra text.
Format exactly like this:
[
  {{
    "question": "Question text here?",
    "answer": "Clear, concise answer here"
  }}
]"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# ── UI ────────────────────────────────────────────────────────
content = st.text_area(
    "📄 Paste Your Training Content Here",
    height=200,
    placeholder="Paste any training material, notes, or topic content here..."
)

col1, col2 = st.columns(2)
with col1:
    num_cards = st.selectbox("🔢 Number of Flashcards", [5, 8, 10, 15])
with col2:
    difficulty = st.selectbox("📊 Difficulty Level", ["Beginner", "Intermediate", "Advanced"])

if st.button("🃏 Generate Flashcards") and content.strip():
    with st.spinner("Creating your flashcards..."):
        raw = generate_flashcards(content, num_cards, difficulty)

    try:
        clean = raw.strip()
        if clean.startswith("```"):
            clean = clean.split("```")[1]
            if clean.startswith("json"):
                clean = clean[4:]
        clean = clean.strip()

        cards = json.loads(clean)

        st.markdown("---")
        st.markdown(f"## 🃏 Your Flashcards ({len(cards)} cards)")
        st.markdown("Click each card to reveal the answer.")

        for i, card in enumerate(cards, 1):
            with st.expander(f"Card {i}: {card['question']}"):
                st.success(f"**Answer:** {card['answer']}")

        # Download
        flashcard_text = "FLASHCARDS\n\n"
        for i, card in enumerate(cards, 1):
            flashcard_text += f"Card {i}\n"
            flashcard_text += f"Q: {card['question']}\n"
            flashcard_text += f"A: {card['answer']}\n\n"

        st.download_button(
            label="⬇️ Download Flashcards",
            data=flashcard_text,
            file_name="flashcards.txt",
            mime="text/plain"
        )

    except json.JSONDecodeError:
        st.error("The AI returned an unexpected format. Please try again.")
        st.code(raw)

st.markdown("---")
st.caption("Built by Meghana · Day 82 · AI Flashcard Generator")