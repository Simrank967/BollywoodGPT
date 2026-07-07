import pandas as pd

from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

df = pd.read_csv("bollywood_news.csv")

docs = []

for _, row in df.iterrows():
    text = f"""
Title: {row['title']}

Summary:
{row['summary']}

"""

    docs.append(
    Document(
        page_content=text,
        metadata={
            "title": row["title"],
            "source": row["source"],
            "link": row["link"]
        }
    )
)

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-base-en-v1.5"
)

vectorstore = FAISS.from_documents(docs, embeddings)

vectorstore.save_local("faiss_index")

print("✅ FAISS index created successfully!")