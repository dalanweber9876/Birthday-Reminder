import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_birthday_message(birthday, tone="short and sweet"):
    prompt = f"Write a short, thoughtful birthday message to {birthday.name}. They are the user's {birthday.relationship}. They would the message to be {tone}."

    if birthday.background:
        prompt += f"\n Here is some background: \n {birthday.background} \n Please use this background to make the message more personal, but you don't need to mention every part of it."

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

    