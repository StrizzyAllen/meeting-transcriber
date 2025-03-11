from app import create_app
import os

print("OpenAI API Key:", os.getenv("OPENAI_API_KEY"))

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
    