import pandas as pd

from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load movie dataset
df = pd.read_csv("data/1950-2019/bollywood_full_1950-2019.csv")

documents = []

for _, row in df.iterrows():

    text = f"""
Title: {row['title_x']}

Original Title: {row['original_title']}

Genres: {row['genres']}

Release Year: {row['year_of_release']}

IMDb Rating: {row['imdb_rating']}

Actors: {row['actors']}

Story:
{row['story']}

Summary:
{row['summary']}

Tagline:
{row['tagline']}
"""

    documents.append(
        Document(
            page_content=text,
            metadata={
                "title": row["title_x"],
                "wiki": row["wiki_link"],
                "poster": row["poster_path"]
            }
        )
    )

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-base-en-v1.5"
)

vectorstore = FAISS.from_documents(documents, embeddings)

vectorstore.save_local("movie_index")

print("✅ Movie FAISS Index Created Successfully!")