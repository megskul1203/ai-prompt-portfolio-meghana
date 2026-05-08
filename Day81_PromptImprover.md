\# Day 81 — AI Prompt Improver

\#\# What I understood today (in my own words)  
A prompt improver is a meta-tool — it uses prompt engineering to teach  
prompt engineering. The quality of the output depended entirely on how  
well I structured the system prompt. I had to use role prompting, format  
specification, and constraint setting in my own prompt to get the AI to  
analyse those same techniques in someone else's prompt.

\#\# What I actually tried  
\- Built a Streamlit app that takes any weak prompt and improves it  
\- Added a use case selector so the AI has context about the domain  
\- Prompted the AI to identify problems, rewrite the prompt, explain  
  changes, and name the techniques used  
\- Fixed an indentation error by replacing the complex section parser  
  with a simpler st.markdown display  
\- Tested with "Write something about leadership for my training"  
\- Output correctly identified 3 problems and applied role prompting,  
  format specification, and constraint setting  
\- Deployed as fourth live app on Streamlit Community Cloud

\#\# One question I still have  
Could I chain this with the Course Generator — improve a prompt  
and immediately use it to generate a course outline?  
