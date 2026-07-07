import streamlit as st
from chatbot import ask_bot
from helpers.news import get_latest_news
from helpers.styles import load_css

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="BollywoodGPT",
    page_icon="🎬",
    layout="wide"
)

load_css()
# ---------------- BANNER ---------------- #

from PIL import Image
import os

#st.write(os.getcwd())   # Temporary (for debugging)

image_path = os.path.join("assets", "banner.png")
#st.write(image_path)    # Temporary (for debugging)

st.image(image_path, use_container_width=True)


st.markdown(
    """
    <h4 style='text-align:center;
               color:#d4af37;
               margin-top:0;'>
        Your Personal AI Assistant for Bollywood
    </h4>
    """,
    unsafe_allow_html=True
)

st.write("")
# -------------------------------------------------
# Session State
# -------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------------------------
# Sidebar
# -------------------------------------------------

with st.sidebar:

    st.title("🎬 BollywoodGPT")

    st.markdown("---")

    st.markdown("### About")

    st.write(
        """
        BollywoodGPT is an AI assistant that answers
        questions about Bollywood using:

        • Latest News
        • Movie Database
        • Wikipedia
        """
    )

    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []

    st.markdown("---")

    st.caption("Made with ❤️ by Simran Kaur")

# -------------------------------------------------
# Header
# -------------------------------------------------

st.markdown("""
<h1 style='text-align:center;
font-size:60px;
color:#D4AF37;'>

🎬 BollywoodGPT

</h1>

<h4 style='text-align:center;
color:white;'>

✨ Your Premium Bollywood AI Assistant ✨

</h4>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Home Screen
# -------------------------------------------------

if len(st.session_state.messages) == 0:

    st.subheader("🔥 Latest Bollywood News")

    latest = get_latest_news()

    for _, row in latest.head(5).iterrows():

        with st.container(border=True):

            col1, col2 = st.columns([1,3])

            with col1:
                if row["image"]:
                    st.image(row["image"], use_container_width=True)

            with col2:

                st.markdown(f"### {row['title']}")

                st.caption(
                    f"📰 {row['source']} • 📅 {row['published'][:10]}"
                )

                st.write(row["summary"])

                st.link_button(
                    "Read Full Article",
                    row["link"]
                )

# -------------------------------------------------
# Previous Chat
# -------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------------------------------
# User Input
# -------------------------------------------------

question = st.chat_input("Ask anything about Bollywood...")

if question:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Searching Bollywood..."):

            answer, docs = ask_bot(question)

        st.markdown(answer)

        if docs:

            with st.expander("📚 Sources"):

                for doc in docs:

                    title = doc.metadata.get("title","Unknown")
                    st.markdown(f"### 🎬 {title}")

                    if "source" in doc.metadata:
                        st.write("📰", doc.metadata["source"])

                    if "year" in doc.metadata:
                        st.write("📅", doc.metadata["year"])

                    if "imdb_rating" in doc.metadata:
                        st.write("⭐", doc.metadata["imdb_rating"])

                    if "genres" in doc.metadata:
                        st.write("🎭", doc.metadata["genres"])

                    if "link" in doc.metadata:
                        st.link_button(
                            "Open Article",
                            doc.metadata["link"]
                        )

                    st.divider()

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )

# -------------------------------------------------
# Footer
# -------------------------------------------------

st.markdown(
"<hr style='border:2px solid #D4AF37;'>",
unsafe_allow_html=True
)

st.markdown("""
<hr style="border:1px solid #D4AF37">

<p style='text-align:center;
color:#D4AF37;'>

🎬 BollywoodGPT

<br>

Powered by Groq • FAISS • HuggingFace

</p>
""", unsafe_allow_html=True)