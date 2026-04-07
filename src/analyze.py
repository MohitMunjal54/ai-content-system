import json
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class PatternAnalyzer:

    def analyze(self):
        # Read collected files
        with open("data/youtube.json") as f:
            yt = json.load(f)
        with open("data/twitter.json") as f:
            tw = json.load(f)
        with open("data/news.json") as f:
            news = json.load(f)

        prompt = f"""
Go through this data and highlight common patterns in viral crypto content.
Focus on:
- Hooks used frequently
- Topics people are interested in right now
- Storytelling style that creators follow
- What gets the most engagement

YouTube: {yt}
Twitter: {tw}
News: {news}
"""

        resp = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return resp.choices[0].message.content
