import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(
    page_title="AI Prompt Improver",
    page_icon="✨",
    layout="centered"
)

st.title("✨ AI Prompt Improver")
st.markdown("Paste any weak prompt and get a professionally structured version instantly.")

@st.cache_resource
def load_client():
    return Groq(api_key=os.getenv("GROQ_API_KEY"))

client = load_client()

def improve_prompt(weak_prompt, use_case):
    prompt = f"""You are an expert prompt engineer with deep knowledge of 
LLM behaviour and prompt design patterns.

A user has written a weak, vague prompt and needs your help improving it.

Use Case / Context: {use_case}
Weak Prompt: {weak_prompt}

Analyse the weak prompt and provide:

PROBLEMS IDENTIFIED:
[List 2-3 specific problems with the original prompt — be specific, not generic]

IMPROVED PROMPT:
[Write a significantly better version of the prompt using these elements where relevant:
- Clear role assignment (You are a...)
- Specific context
- Precise task description
- Output format instructions
- Constraints or tone guidance]

WHAT CHANGED AND WHY:
[Explain 3-4 specific improvements you made and the reasoning behind each change]

PROMPT ENGINEERING TECHNIQUE USED:
[Name the technique(s) applied — e.g. Role prompting, Few-shot, Chain of thought, 
Format specification, Constraint setting]"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

use_case = st.selectbox(
    "🎯 What is this prompt for?",
    [
        "Content Writing",
        "Learning & Development / Training",
        "Customer Support",
        "Data Analysis",
        "Code Generation",
        "Marketing / Copywriting",
        "HR / Recruitment",
        "General Purpose"
    ]
)

weak_prompt = st.text_area(
    "📝 Paste Your Weak Prompt Here",
    height=150,
    placeholder="e.g. Write something about leadership for my training..."
)

if st.button("✨ Improve My Prompt") and weak_prompt.strip():
    with st.spinner("Analysing and improving your prompt..."):
        result = improve_prompt(weak_prompt, use_case)

    st.markdown("---")
    st.markdown("## ✅ Improved Prompt Analysis")
    st.markdown(result)

    st.download_button(
        label="⬇️ Download Full Analysis",
        data=result,
        file_name="improved_prompt.txt",
        mime="text/plain"
    )

st.markdown("---")
st.caption("Built by Meghana · Day 81 · AI Prompt Improver")