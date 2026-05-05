import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(
    page_title="AI Course Content Generator",
    page_icon="📚",
    layout="centered"
)

st.title("📚 AI Course Content Generator")
st.markdown("Built for L&D professionals — generate a complete course outline in seconds.")

@st.cache_resource
def load_client():
    return Groq(api_key=os.getenv("GROQ_API_KEY"))

client = load_client()

def generate_course(topic, audience, duration, level):
    prompt = f"""You are an expert instructional designer with 10 years of experience 
creating corporate training programs.

Create a complete course outline for the following:
- Topic: {topic}
- Target Audience: {audience}
- Course Duration: {duration}
- Difficulty Level: {level}

Structure your response exactly like this:

COURSE TITLE:
[A compelling title for the course]

COURSE DESCRIPTION:
[2-3 sentences describing what this course covers and why it matters]

LEARNING OBJECTIVES:
By the end of this course, learners will be able to:
1. [Objective 1 — use action verbs like analyze, apply, create, evaluate]
2. [Objective 2]
3. [Objective 3]
4. [Objective 4]

MODULE BREAKDOWN:
Module 1: [Module Title]
- Subtopic 1
- Subtopic 2
- Subtopic 3

Module 2: [Module Title]
- Subtopic 1
- Subtopic 2
- Subtopic 3

Module 3: [Module Title]
- Subtopic 1
- Subtopic 2
- Subtopic 3

Module 4: [Module Title]
- Subtopic 1
- Subtopic 2
- Subtopic 3

ASSESSMENT STRATEGY:
[Describe 2-3 ways to assess learner understanding — quizzes, projects, scenarios]

RECOMMENDED TOOLS/RESOURCES:
[List 3-4 tools or resources that would support this course]"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# UI
col1, col2 = st.columns(2)

with col1:
    topic = st.text_input("📌 Course Topic", placeholder="e.g. Python for beginners")
    duration = st.selectbox("⏱ Course Duration", [
        "1 hour", "half day", "1 day", "2 days", "1 week", "4 weeks"
    ])

with col2:
    audience = st.text_input("👥 Target Audience", placeholder="e.g. Working professionals with no coding background")
    level = st.selectbox("📊 Difficulty Level", [
        "Beginner", "Intermediate", "Advanced", "Mixed"
    ])

if st.button("🎯 Generate Course Outline") and topic.strip() and audience.strip():
    with st.spinner("Designing your course..."):
        result = generate_course(topic, audience, duration, level)
    
    st.markdown("---")
    st.markdown("## 📋 Your Course Outline")
    st.markdown(result)
    
    st.download_button(
        label="⬇️ Download Course Outline",
        data=result,
        file_name=f"{topic.replace(' ', '_')}_course_outline.txt",
        mime="text/plain"
    )

st.markdown("---")
st.caption("Built by Meghana · Day 78 · AI Course Content Generator")