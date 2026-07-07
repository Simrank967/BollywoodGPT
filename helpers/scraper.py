import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GNEWS_API_KEY")

url = (
    f"https://gnews.io/api/v4/search?"
    f"q=bollywood&"
    f"lang=en&"
    f"country=in&"
    f"max=50&"
    f"apikey={API_KEY}"
)

response = requests.get(url)
data = response.json()

articles = []

for article in data.get("articles", []):

    articles.append({
        "title": article["title"],
        "summary": article["description"],
        "content": article["content"],
        "image": article["image"],
        "published": article["publishedAt"],
        "link": article["url"],
        "source": article["source"]["name"]
    })

df = pd.DataFrame(articles)

os.makedirs("data", exist_ok=True)

df.to_csv("data/bollywood_news.csv", index=False)

print(f"✅ Saved {len(df)} articles")