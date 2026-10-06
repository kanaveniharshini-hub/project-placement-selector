import streamlit as st
from chatbot import chatbot_response

st.set_page_config(
    page_title="Placement Preparation Chatbot",
    page_icon="🎓"
)

st.title("🎓 Student Placement Preparation System")

st.write("Your personal placement preparation assistant 🤖")

# Sidebar
st.sidebar.title("📚 Preparation Menu")

st.sidebar.write("You can ask about:")

st.sidebar.write("📊 Aptitude")
st.sidebar.write("💻 Coding")
st.sidebar.write("🎯 Interviews")
st.sidebar.write("📄 Resume")
st.sidebar.write("🗺️ Roadmap")
st.sidebar.write("🐍 Python")
st.sidebar.write("☕ Java")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input(
    "Ask your placement question..."
)

if user_input:

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Get chatbot response
    response = chatbot_response(user_input)

    # Display bot response
    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })