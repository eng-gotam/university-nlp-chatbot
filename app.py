
import streamlit as st
from chatbot import get_chatbot_response

st.set_page_config(
    page_title="University NLP Chatbot",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 University Student Support Chatbot")

st.caption(
    "Ask questions about admissions, fees, "
    "scholarships, and university contacts."
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! How can I help you today?"
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Type your question here..."):

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    response = get_chatbot_response(prompt)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.write(response)
