\# Day 84 — AI Job Description Analyser

\#\# What I Built  
An AI tool that takes any job description and maps it against my profile.  
Outputs: required skills, gap analysis, strength mapping, tailored pitch,  
and 5 likely interview questions — all personalised to me.

\#\# What I Learned  
\- Functions are reusable SOPs — define once, call many times  
\- Default parameters make functions flexible without breaking them  
\- @st.cache\_resource loads heavy resources once and remembers them  
\- @st.cache\_data reuses outputs for identical inputs  
\- call\_ai() is a function I now use across every project  
\- Keeping my profile as a constant (MEGHANA\_PROFILE) means  
  I update it once and every prompt benefits automatically

\#\# How I'd Explain This in an Interview  
"I built a JD analyser that takes any job description and maps it against  
my background using an LLM. It extracts required skills, identifies gaps,  
highlights my strengths for that specific role, and generates a tailored  
pitch. I use it myself to prepare for every application — including this one."  
