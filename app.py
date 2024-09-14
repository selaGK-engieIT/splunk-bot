import streamlit as st
from pages import chat, home, faq, settings, feedback

def sidebar():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "Chat", "FAQ / Help", "Settings", "Feedback"])
    return selection

def main():
    page = sidebar()
    if page == "Home":
        home.display()
    elif page == "Chat":
        chat.display()
    elif page == "FAQ / Help":
        faq.display()
    elif page == "Settings":
        settings.display()
    elif page == "Feedback":
        feedback.display()

if __name__ == '__main__':
    main()
