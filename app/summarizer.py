import openai
from config import OPENAI_API_KEY

print(f"🔑 Debug: OpenAI API Key Loaded - {OPENAI_API_KEY[:10]}... (truncated)")  # Print first 10 characters

openai.api_key = OPENAI_API_KEY

def summarize_text(text):
    response = openai.ChatCompletion.create(  # Corrected API call
        model="gpt-4.5-preview",
        messages=[
            {"role": "system", "content": "You are an AI that summarizes meeting transcripts."},
            {"role": "user", "content": f"Summarize this meeting transcript:\n{text}"}
        ]
    )
    return response["choices"][0]["message"]["content"]  # Corrected response parsing
