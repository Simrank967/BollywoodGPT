import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from helpers.wikipedia_helper import get_actor_info
load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-base-en-v1.5"
)

news_store = FAISS.load_local(
    "vector_store/faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

movie_store = FAISS.load_local(
    "vector_store/movie_index",
    embeddings,
    allow_dangerous_deserialization=True
)

news_retriever = news_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k":3,
        "fetch_k":8,
        "lambda_mult":0.5
    }
)

movie_retriever = movie_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k":3,
        "fetch_k":8,
        "lambda_mult":0.5
    }
)
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile",
    temperature=0
)

prompt = ChatPromptTemplate.from_template("""
You are BollywoodGPT, an expert Bollywood assistant.

Use the retrieved news articles when they are relevant.

If the articles only partially answer the question,
combine them with your own knowledge.

For biography questions, provide a concise overview.

For news questions, answer only from the retrieved articles.

If the answer cannot be found anywhere, say:
"I couldn't find reliable information."

Context:
{context}

Question:
{question}

Answer:
""")

chain = prompt | llm


def ask_bot(question):

    # Detect actor name (even if misspelled)
    actor = question

    wiki = None

    if actor:
        wiki = get_actor_info(actor)

    # Search news
    news_docs = news_retriever.invoke(question)
    movie_docs = movie_retriever.invoke(question)

    docs = movie_docs + news_docs
    context = "\n\n".join(doc.page_content for doc in docs)

    response = chain.invoke({
        "context": context,
        "question": question
    })

    answer = response.content

    # Add Wikipedia biography
    if wiki:
        answer = f"""
## 👤 {wiki['title']}

{wiki['summary']}

---

## 📰 Latest News

{answer}
"""

    return answer, docs