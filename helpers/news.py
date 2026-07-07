import pandas as pd

def get_latest_news(n=10):
    df = pd.read_csv("data/bollywood_news.csv")

    # remove duplicate articles
    df = df.drop_duplicates(subset=["title"])

    return df.head(n)