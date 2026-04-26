# **Day 69 — Meghana's Python Reboot**

## **Complete Record of What I Did, What I Learned, and What's Next**

---

## **What I Accomplished Today**

In one sitting, starting from zero, I:

* Installed and configured a professional coding environment (VS Code)  
* Wrote and ran my first Python file  
* Debugged 6 real errors like a working developer  
* Made a real AI API call and received a response  
* Learned why API keys must never go in code  
* Installed and used Git for the first time  
* Pushed my first `.py` file to GitHub using the command line

This is the first day in 69 days that my GitHub repo contains **runnable code**, not just documentation.

---

## **What I Set Up — And Why**

### **VS Code**

VS Code (Visual Studio Code) is a code editor made by Microsoft. Think of it like Microsoft Word, but for writing code. It gives you:

* **Colour coding** — different parts of code appear in different colours so you can read it easily  
* **Error highlighting** — underlines mistakes in red before you even run the code  
* **Auto-complete** — suggests what you're typing  
* **Integrated terminal** — run your code without switching windows

It is the industry standard editor. Every developer at Freshworks, Sarvam AI, and similar companies uses VS Code or something equivalent.

### **Python Extension**

VS Code is a blank editor by default — it doesn't assume which language you'll use. The Python extension by Microsoft teaches VS Code what Python code looks like, so it can highlight errors, colour the syntax correctly, and run Python files.

**Analogy:** VS Code is the LMS platform. The Python extension is the course content loaded into it. Without the content, the platform is an empty shell.

### **Git**

Git is a version control system. Every time you say `git commit`, it takes a snapshot of your project. Think of it like saving named versions of a document — except smarter, automatic, and trackable by anyone.

* `git init` — start tracking a folder  
* `git add .` — select files for the next snapshot  
* `git commit -m "message"` — take the snapshot with a label  
* `git push` — send the snapshot to GitHub online

### **GitHub vs Git**

* **Git** \= your camera (takes snapshots on your computer)  
* **GitHub** \= Google Photos (stores them online, makes them shareable)

Your existing 68 days were uploaded manually through the browser. From Day 69, you are committing through Git like a developer. Recruiters can see the difference immediately.

---

## **What I Built — The Code Explained Line by Line**

from groq import Groq          \# Import the Groq library — like opening an app before using it  
import os                      \# Import the os library — lets Python talk to your computer's settings  
from dotenv import load\_dotenv \# Import dotenv — lets Python read your .env secrets file

load\_dotenv()                  \# Read the .env file and load the variables into memory

client \= Groq(                 \# Create a connection to Groq's servers  
    api\_key=os.environ.get("GROQ\_API\_KEY")  \# Use the key from environment, not hardcoded  
)

response \= client.chat.completions.create(   \# Send a message to the AI  
    model="llama-3.3-70b-versatile",         \# Use this specific AI model (Llama 3.3 by Meta)  
    messages=\[  
        {"role": "user",                     \# This message is from the user (me)  
         "content": "What is RAG (Retrieval Augmented Generation) in AI in 2 sentences?"}  
    \]  
)

print(response.choices\[0\].message.content)  \# Print what the AI said back

### **What the AI returned:**

"RAG (Retrieval Augmented Generation) is a type of artificial intelligence framework that combines the strengths of retrieval-based and generation-based models to produce more accurate and informative outputs. By leveraging a retrieval component to fetch relevant information from a knowledge base and a generation component to create text based on the retrieved information, RAG models can generate more coherent and context-specific text."

This is the concept from Day 11 of my portfolio — now confirmed by a live AI model that my own Python code called.

---

## **The 6 Errors I Debugged — And What Each One Taught Me**

### **Error 1 — OpenAI quota exceeded (429)**

**What happened:** My OpenAI free account had no credits.  
 **What I learned:** Free tier APIs have limits. Always check billing before relying on a service.

### **Error 2 — Google deprecated library**

**What happened:** `google.generativeai` package is no longer supported.  
 **What I learned:** AI libraries change fast. Always check the official docs for the current package name.

### **Error 3 — Wrong model name (gemini-2.0-flash not available on free tier)**

**What happened:** `limit: 0` in the error — the model wasn't free.  
 **What I learned:** Not all AI models are available on free accounts. Read the rate limits page.

### **Error 4 — Groq model decommissioned (llama3-8b-8192)**

**What happened:** The model I used was retired.  
 **What I learned:** AI models get deprecated regularly. Always check the current model list.

### **Error 5 — API key hardcoded in code (GitHub rejected the push)**

**What happened:** GitHub's Push Protection detected my Groq API key inside the code and blocked the push.  
 **What I learned:** Never paste API keys directly in code. Use environment variables and `.env` files. This is a professional security practice, not just a rule.

### **Error 6 — dotenv module not found**

**What happened:** I hadn't installed the `python-dotenv` library yet.  
 **What I learned:** Every library needs to be installed with `pip install` before you can use it. The import line in your code and the pip install are two separate steps.

---

## **Key Concepts I Now Understand By Doing (Not Just Reading)**

### **API (Application Programming Interface)**

A way for your code to talk to someone else's service over the internet. Your Python code sends a request → Groq's servers receive it → AI generates a response → sends it back → your code prints it.

Like calling a restaurant on the phone — you (code) call them (API), place an order (prompt), they make the food (AI processes), and deliver it (response).

### **API Key**

Your unique password that proves your identity to the API provider. Without it, the server doesn't know who you are or whether to respond. It must be kept secret — never put it in code that goes on GitHub.

### **Environment Variables**

A way to store secret values on your computer without putting them in your code. The `.env` file stores your key. `os.environ.get("GROQ_API_KEY")` reads it. Your code stays clean and shareable.

### **pip install**

The command that downloads and installs Python libraries from the internet. Like an app store for Python tools.

### **Git commit**

A saved snapshot of your project at a specific point in time, with a label. Your Day 69 commit message: `"Day 69: Python reboot — first real AI API call using Groq"` — this appears on your GitHub profile permanently.

---

## **What I Understood Today (In My Own Words)**

Python runs directly on my computer. VS Code is the workspace where I write it. The terminal is where I see the output. An API is a bridge between my code and an AI model living on someone else's servers. The API key is my access pass for that bridge. Environment variables keep the key secret while still letting the code use it. Git takes snapshots of my work. GitHub stores those snapshots online so anyone — including recruiters — can see them.

---

## **One Question I Had (Answered)**

**Q: How does the API key stay secure if I paste it in my code?**  
 **A:** It doesn't — that's the whole point. You never paste the key in your code. You store it in a `.env` file on your computer, add `.env` to `.gitignore` (so Git never uploads it), and read it in your code using `os.environ.get()`. GitHub even has automated protection that scans every push for exposed keys and blocks it — which I experienced firsthand today on Error 5\.

## **Day 69 Stats**

* Hours invested: \~4 hours  
* Errors debugged: 6  
* Python concepts used: variables, f-strings, functions, imports, print  
* Files committed to GitHub: 1 (first ever .py file)  
* APIs attempted: 3 (OpenAI, Google Gemini, Groq)  
* API that worked: Groq ✅  
* Commit message: `"Day 69: Python reboot — first real AI API call using Groq"`

---

*Day 69 complete. The repository now contains real, runnable code for the first time.*  
 *Next commit: Day 70 — Prompt templates and loops.*

