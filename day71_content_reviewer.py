from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Step 1 — Read the content file
with open("sample_content.txt", "r") as f:
    content = f.read()

print("Content loaded successfully!")
print(f"Total characters: {len(content)}")
print("\nSending to AI for review...\n")

# Step 2 — Review function
def review_content(text):
    prompt = f"""You are an expert L&D content reviewer.
Review the following training content and give feedback on:

1. Clarity — is it easy to understand for a beginner?
2. Structure — is it well organised?
3. One specific suggestion to improve it

Training content:
{text}"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Step 3 — Run the review and save output
feedback = review_content(content)

print("=== AI FEEDBACK ===")
print(feedback)

# Step 4 — Save feedback to a new file
with open("feedback_output.txt", "w") as f:
    f.write("AI CONTENT REVIEW FEEDBACK\n")
    f.write("="*40 + "\n\n")
    f.write("ORIGINAL CONTENT:\n")
    f.write(content)
    f.write("\n\n" + "="*40 + "\n\n")
    f.write("AI FEEDBACK:\n")
    f.write(feedback)

print("\nFeedback saved to feedback_output.txt!")