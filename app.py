import streamlit as st
from agent import agentic_response

st.set_page_config(page_title="Chatbot", layout="wide")

if "history" not in st.session_state:
    st.session_state.history = []

if "reflection" not in st.session_state:
    st.session_state.reflection = True

st.title("Chatbot")

st.session_state.reflection = st.checkbox("Show Reflection", True)
for chat in st.session_state.history:
    role = "user" if chat["sender"] == "user" else "assistant"
    st.chat_message(role).write(chat["message"])
    
user_input = st.chat_input("Ask something...")

if user_input:
    st.session_state.history.append({"sender": "user", "message": user_input})

    with st.spinner("Thinking..."):
        reply = agentic_response(
            user_input,
            st.session_state.history,
            st.session_state.reflection
        )

    st.session_state.history.append({"sender": "bot", "message": reply})
    st.rerun()