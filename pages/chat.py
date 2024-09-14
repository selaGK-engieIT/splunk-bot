import streamlit as st
from utils.chatbot_logic import get_chatbot_response 

chat_history = []

def display():
    st.title("Chat with ChatGPT")

    for chat in chat_history:
        st.write(f"{chat}")

    user_input = st.text_input("Type your message:")
    
    if st.button("Send"):
        if user_input:
            chat_history.append(f"You: {user_input}")
            bot_response = get_chatbot_response(user_input)
            chat_history.append(bot_response)
            st.experimental_rerun()  # Refresh the chat to show new messages
