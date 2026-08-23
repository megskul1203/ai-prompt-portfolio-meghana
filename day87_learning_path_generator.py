import streamlit as st
import os
import json
import re
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "openai/gpt-oss-120b"

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
    page_title="AI Learning Path Generator",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ AI Learning Path Generator")
st.caption("Enter any skill → get a personalised week-by-week learning plan with resources and milestones")
st.divider()

# ── Inputs ────────────────────────────────────────────────────────────────────
col1, col2 = st.columns(2)
with col1:
    skill = st.text_input(
        "What skill do you want to learn?",
        placeholder="e.g. Prompt Engineering, Python, Data Analysis, Public Speaking..."
    )
    current_level = st.selectbox(
        "Your current level",
        ["Complete Beginner", "Some Basics", "Intermediate", "Advanced — deepening knowledge"]
    )
with col2:
    goal = st.text_area(
        "What is your learning goal?",
        height=100,
        placeholder="e.g. Get a job as a Prompt Engineer, build AI apps, pass a certification exam..."
    )
    weeks = st.slider("How many weeks do you have?", 2, 12, 4)

col3, col4 = st.columns(2)
with col3:
    hours_per_week = st.selectbox(
        "Hours available per week",
        ["1-2 hours", "3-5 hours", "5-10 hours", "10+ hours"]
    )
with col4:
    learning_style = st.selectbox(
        "Preferred learning style",
        ["Videos and tutorials", "Reading and documentation",
         "Hands-on projects", "Mixed — a bit of everything"]
    )

generate_btn = st.button("🗺️ Generate My Learning Path", type="primary")

# ── Generation ────────────────────────────────────────────────────────────────
if generate_btn:
    if not skill.strip():
        st.warning("Please enter a skill you want to learn.")
    elif not goal.strip():
        st.warning("Please enter your learning goal.")
    else:
        with st.spinner("Building your personalised learning path..."):

            system = """You are an expert instructional designer and curriculum developer 
            with deep knowledge of self-directed learning, Bloom's Taxonomy, and online 
            learning resources. You create structured, achievable, and practical learning paths."""

            prompt = f"""
Create a detailed week-by-week learning path for someone who wants to learn:

Skill: {skill}
Current Level: {current_level}
Goal: {goal}
Duration: {weeks} weeks
Hours per week: {hours_per_week}
Learning Style: {learning_style}

Apply Bloom's Taxonomy — start with Remember/Understand in early weeks,
move to Apply/Analyse in middle weeks, and Create/Evaluate in final weeks.

Respond ONLY with valid JSON. No extra text. Format:
{{
  "skill": "{skill}",
  "total_weeks": {weeks},
  "goal": "{goal}",
  "overview": "2-3 sentence summary of this learning journey and what the learner will achieve",
  "weekly_plans": [
    {{
      "week": 1,
      "theme": "short theme title for this week",
      "bloom_level": "Remember / Understand / Apply / Analyse / Evaluate / Create",
      "learning_objectives": [
        "By end of this week, learner will be able to... (use Bloom's verb)",
        "By end of this week, learner will be able to..."
      ],
      "topics": ["topic 1", "topic 2", "topic 3"],
      "resources": [
        {{
          "title": "resource name",
          "type": "Video / Article / Documentation / Course / Book",
          "url": "actual URL if you know it, otherwise describe where to find it",
          "duration": "estimated time e.g. 30 mins"
        }}
      ],
      "milestone": "concrete thing the learner should be able to DO by end of this week",
      "mini_task": "a small practical task to complete this week (hands-on)"
    }}
  ],
  "final_project": {{
    "title": "capstone project title",
    "description": "what the learner will build or create to validate their learning",
    "skills_demonstrated": ["skill 1", "skill 2", "skill 3"]
  }},
  "success_metrics": [
    "how the learner will know they've succeeded metric 1",
    "how the learner will know they've succeeded metric 2",
    "how the learner will know they've succeeded metric 3"
  ]
}}
"""
            raw = call_ai(prompt, system)

        try:
            data = extract_json(raw)

            # ── Header ────────────────────────────────────────────────────────
            st.success("Your learning path is ready!")
            st.subheader(f"🎯 Learning Path: {data.get('skill', skill)}")
            st.info(f"**Goal:** {data.get('goal', goal)}")
            st.write(data.get("overview", ""))
            st.divider()

            # ── Weekly Plans ──────────────────────────────────────────────────
            st.subheader(f"📅 Your {data.get('total_weeks', weeks)}-Week Plan")

            weekly_plans = data.get("weekly_plans", [])

            # Progress bar visual
            cols = st.columns(len(weekly_plans))
            for i, week in enumerate(weekly_plans):
                with cols[i]:
                    bloom = week.get("bloom_level", "")
                    color_map = {
                        "Remember": "🟦",
                        "Understand": "🟩",
                        "Apply": "🟨",
                        "Analyse": "🟧",
                        "Evaluate": "🟥",
                        "Create": "🟪"
                    }
                    icon = next((v for k, v in color_map.items() if k.lower() in bloom.lower()), "⬜")
                    st.markdown(f"**Week {week.get('week')}**")
                    st.caption(f"{icon} {bloom}")
                    st.caption(week.get("theme", ""))

            st.divider()

            # ── Week by week detail ───────────────────────────────────────────
            for week in weekly_plans:
                week_num = week.get("week", "")
                theme = week.get("theme", "")
                bloom = week.get("bloom_level", "")

                with st.expander(f"📅 Week {week_num}: {theme}  —  Bloom's Level: {bloom}", expanded=(week_num == 1)):

                    col_a, col_b = st.columns(2)

                    with col_a:
                        st.markdown("**🎯 Learning Objectives**")
                        for obj in week.get("learning_objectives", []):
                            st.write(f"• {obj}")

                        st.markdown("**📖 Topics This Week**")
                        for topic in week.get("topics", []):
                            st.write(f"• {topic}")

                    with col_b:
                        st.markdown("**📚 Resources**")
                        for res in week.get("resources", []):
                            res_type = res.get("type", "")
                            res_title = res.get("title", "")
                            res_url = res.get("url", "")
                            res_dur = res.get("duration", "")

                            type_icons = {
                                "Video": "🎥", "Article": "📄",
                                "Documentation": "📋", "Course": "🎓", "Book": "📚"
                            }
                            icon = next((v for k, v in type_icons.items() if k.lower() in res_type.lower()), "🔗")

                            if res_url and res_url.startswith("http"):
                                st.markdown(f"{icon} [{res_title}]({res_url}) — *{res_dur}*")
                            else:
                                st.markdown(f"{icon} **{res_title}** — *{res_dur}*")
                                if res_url:
                                    st.caption(f"Find at: {res_url}")

                    st.divider()

                    col_c, col_d = st.columns(2)
                    with col_c:
                        st.success(f"✅ **Week Milestone:** {week.get('milestone', '')}")
                    with col_d:
                        st.info(f"🛠️ **Mini Task:** {week.get('mini_task', '')}")

            # ── Final Project ─────────────────────────────────────────────────
            st.divider()
            final = data.get("final_project", {})
            st.subheader("🏆 Final Capstone Project")
            st.markdown(f"**{final.get('title', '')}**")
            st.write(final.get("description", ""))
            st.markdown("**Skills you'll demonstrate:**")
            for s in final.get("skills_demonstrated", []):
                st.write(f"• {s}")

            # ── Success Metrics ───────────────────────────────────────────────
            st.divider()
            st.subheader("📊 How You'll Know You've Succeeded")
            for metric in data.get("success_metrics", []):
                st.write(f"✅ {metric}")

            # ── Download ──────────────────────────────────────────────────────
            st.divider()

            # Plain text version for download
            text_output = f"LEARNING PATH: {data.get('skill', skill)}\n"
            text_output += f"Goal: {data.get('goal', goal)}\n"
            text_output += f"Duration: {data.get('total_weeks', weeks)} weeks\n\n"
            text_output += f"Overview:\n{data.get('overview', '')}\n\n"

            for week in weekly_plans:
                text_output += f"\nWEEK {week.get('week')}: {week.get('theme')}\n"
                text_output += f"Bloom's Level: {week.get('bloom_level')}\n"
                text_output += "Learning Objectives:\n"
                for obj in week.get("learning_objectives", []):
                    text_output += f"  • {obj}\n"
                text_output += f"Milestone: {week.get('milestone', '')}\n"
                text_output += f"Mini Task: {week.get('mini_task', '')}\n"

            text_output += f"\nFINAL PROJECT: {final.get('title', '')}\n"
            text_output += final.get("description", "")

            st.download_button(
                "⬇️ Download Learning Path (.txt)",
                data=text_output,
                file_name=f"learning_path_{skill.replace(' ', '_')}.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Could not parse AI response. Please try again. ({e})")
            with st.expander("Raw AI response"):
                st.text(raw)

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption("Built by Meghana · Day 87 of 90 · AI Learning Path Generator · Groq + Streamlit")