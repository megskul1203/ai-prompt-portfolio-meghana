\# Day 85 — AI Job Search Agent

\#\# What I Built  
A live job search agent that fetches real jobs from LinkedIn, Indeed, and  
Glassdoor using JSearch API, then uses AI to analyse each job against my  
profile — giving fit scores, gap analysis, salary estimates, and a  
one-line pitch for every result.

\#\# What I Learned  
\- APIs are structured request windows — you send parameters, get back JSON  
\- requests.get() is how Python talks to any REST API, not just Groq  
\- @st.cache\_data saves API responses so I do not waste free tier calls  
\- Two APIs can work together — JSearch fetches jobs, Groq analyses them  
\- Real-time data plus AI analysis equals genuinely useful tools

\#\# How I'd Explain This in an Interview  
"I built a job search agent that combines two APIs — JSearch for live job  
data and Groq's LLaMA model for intelligent fit analysis. It fetches real  
jobs, scores them against my profile, and generates tailored pitches  
automatically. I built it because I needed it — which is the best reason  
to build anything."  
