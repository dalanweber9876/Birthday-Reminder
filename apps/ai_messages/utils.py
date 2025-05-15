import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_birthday_message(birthday):
    prompt = f"Write a short, thoughtful birthday message to {birthday.name}. They are the user's {birthday.relationship}"

    if birthday.background:
        prompt += f"\n Here is some background: \n {birthday.background}"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating message: {e}"

    