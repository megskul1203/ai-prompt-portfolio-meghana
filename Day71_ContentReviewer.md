\#\# Day 71: AI Content Reviewer — Reading Files \+ Saving Outputs

\#\#\# What I understood today (in my own words)  
\`open()\` is how Python reads files from your computer. The \`with\` keyword   
opens the file, reads it, and closes it automatically — like picking up a   
document, reading it, and putting it back safely. Using \`"r"\` mode means   
read-only, \`"w"\` mode means write — Python creates a new file automatically   
if it doesn't exist. Triple quotes \`"""\` let you write long prompts across   
multiple lines cleanly. \`len()\` counts how many characters are in any text   
or list — a simple but useful tool.

\#\#\# What I actually tried  
Built an AI Content Reviewer that:  
\- Reads \`sample\_content.txt\` from the computer (819 characters loaded)  
\- Sends the content to Llama 3.3 via Groq API with an L\&D reviewer prompt  
\- Gets structured feedback on clarity, structure, and one improvement suggestion  
\- Automatically saves the full review to \`feedback\_output.txt\`

The AI correctly identified that adding a real workplace example would   
strengthen the training module — the same feedback an experienced L\&D   
reviewer would give.

Key learning: the prompt used triple quotes and dropped the entire file   
content into it using {text}. One prompt template, works on any document.

\#\#\# One question I still have  
Can I loop through multiple content files in a folder and review all of   
them in one run — instead of changing the filename manually each time?  
(This would make it a batch content reviewer — next goal)

\#\#\# Real world value  
This tool works on any training content right now. Paste any L\&D material   
into sample\_content.txt, run the script, get instant professional feedback   
saved to a file. Built in 30 minutes. Directly usable at my current job.  
