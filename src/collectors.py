import json
import requests
from bs4 import BeautifulSoup
import subprocess

class DataCollector:

    def collect_youtube(self, query="crypto", limit=5):
        # Fetch YouTube metadata using yt-dlp
        print("Fetching YouTube videos...")
        cmd = ["yt-dlp", f"ytsearch{limit}:{query}", "--dump-json"]
        result = subprocess.run(cmd, capture_output=True, text=True)

        items = []
        for line in result.stdout.splitlines():
            try:
                items.append(json.loads(line))
            except:
                pass

        with open("data/youtube.json", "w") as f:
            json.dump(items, f, indent=2)

        return items

    def collect_twitter(self, query="crypto", limit=20):
        print("Fetching tweets...")
        cmd = f"snscrape --max-results {limit} twitter-search '{query}'"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        tweets = []
        for line in result.stdout.splitlines():
            try:
                tweets.append(json.loads(line))
            except:
                pass

        with open("data/twitter.json", "w") as f:
            json.dump(tweets, f, indent=2)

        return tweets

    def collect_news(self, url="https://cointelegraph.com/"):
        print("Scraping news...")
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")

        headlines = [h.get_text().strip() for h in soup.find_all("h2")]

        with open("data/news.json", "w") as f:
            json.dump(headlines, f, indent=2)

        return headlines
