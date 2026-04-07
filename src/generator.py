from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class IdeaGenerator:

    def generate(self, insights):
        prompt = f"""
Using these insights:
{insights}

Create:
- 5 Instagram reel ideas
- 3 YouTube video ideas
- 3 Twitter thread ideas

For each, include:
- Hook
- Topic
- Brief storyline
"""

        resp = client.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role": "user", "content": prompt}]
        )

        return resp.choices[0].message.content
