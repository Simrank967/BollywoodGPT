import streamlit as st

def load_css():

    st.markdown("""
    <style>

    .stApp{
        background:#0b0b0b;
        color:white;
    }

    section[data-testid="stSidebar"]{
        background:#111111;
        border-right:1px solid #b8860b;
    }

    h1,h2,h3{
        color:#FFD700;
    }

    .stButton>button{
        background:#1c1c1c;
        color:#FFD700;
        border:1px solid #FFD700;
        border-radius:12px;
    }

    .stButton>button:hover{
        background:#FFD700;
        color:black;
    }

    .stChatMessage{
        border-radius:18px;
        padding:15px;
        border:1px solid #2d2d2d;
    }

    .stTextInput>div>div>input{
        background:#161616;
        color:white;
    }

    .stChatInput{
        background:#161616;
    }

    div[data-testid="stExpander"]{
        border:1px solid #333;
        border-radius:10px;
    }

    </style>
    """, unsafe_allow_html=True)