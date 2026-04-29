from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# This list stores the entire conversation history
# It grows with every message — that's how memory works
messages = [
    {
        "role": "system",
        "content": """You are an expert AI tutor helping Meghana, 
an L&D professional transitioning into AI engineering. 
Explain concepts clearly and simply. 
When she asks about AI topics, connect them to L&D wherever possible."""
    }
]

print("=" * 50)
print("AI Tutor Chatbot — Day 72")
print("Your personal AI tutor. Type 'quit' to exit.")
print("=" * 50)
print()

while True:
    # Get user input
    user_input = input("You: ")
    
    # Exit condition
    if user_input.lower() == "quit":
        print("Goodbye! Great learning session.")
        break
    
    # Skip empty inputs
    if user_input.strip() == "":
        continue
    
    # Add user message to history
    messages.append({
        "role": "user",
        "content": user_input
    })
    
    # Send entire history to AI
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    
    # Get AI reply
    reply = response.choices[0].message.content
    
    # Add AI reply to history too
    messages.append({
        "role": "assistant",
        "content": reply
    })
    
    # Print the reply
    print(f"\nAI: {reply}\n")
    
    # Show how many messages in memory
    print(f"[Memory: {len(messages)} messages in conversation]\n")