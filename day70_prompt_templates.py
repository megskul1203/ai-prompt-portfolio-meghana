from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def ask_ai(topic, audience):
    prompt = f"Explain {topic} to a {audience} in 2 simple sentences."
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

topics = [
    ("RAG (Retrieval Augmented Generation)", "non-technical manager"),
    ("Vector Search", "L&D professional"),
    ("Prompt Engineering", "fresh graduate"),
    ("Hallucination in AI", "HR team"),
    ("Fine-tuning vs RAG", "product manager")
]

for topic, audience in topics:
    print(f"\n--- Explaining {topic} to a {audience} ---")
    answer = ask_ai(topic, audience)
    print(answer)