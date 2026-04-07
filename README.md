# ai-content-system

# AI-Powered Viral Crypto Content Generator

This project is a small AI system that helps generate viral content ideas for crypto creators.  
The goal is to automate the first part of the content workflow: collecting trending content, identifying patterns, and producing ideas for Instagram, YouTube, and Twitter.

I kept the design simple so it can run easily on any local machine.

---

## 1. How It Works

The system runs in three steps:

## a) Collect Viral Content
It collects crypto-related content from:
- YouTube (via `yt-dlp`)
- Twitter/X (via `snscrape`)
- Crypto news sites (via BeautifulSoup)

The collected data is saved in the `data/` folder:
- `youtube.json`
- `twitter.json`
- `news.json`

This gives us the raw material to understand what people are engaging with.

---

### b) Analyze Patterns
Once all content is collected, the system sends this dataset to an LLM.

The model identifies:
- Common hooks used in viral posts  
- Topics that are trending  
- Story styles creators use  
- Themes that generate the most engagement  

These insights act as the logic behind idea generation.

---

###  c) Generate Content Ideas
Using the extracted insights, the system generates:
- 5 Instagram reel ideas  
- 3 YouTube video ideas  
- 3 Twitter thread ideas  

Each idea contains:
- A hook  
- Topic  
- Short storyline  

The output is shown directly in the terminal.

---

## 2. Folder Structure
ai-content-system/ ├── data/ ├── src/ │    ├── collectors.py │    ├── analyze.py │    ├── generator.py │    └── main.py ├── requirements.txt └── README.md
---

## 3. Installation

Make sure Python 3.9+ is installed.
Open bash or terminal 
pip install -r requirements.txt
OPENAI_API_KEY=your_api_key_here
---------
## To run the project 
python src/main.py

This will:
Fetch viral content
Analyze it
Generate content ideas.
