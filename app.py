import streamlit as st
from pages import chat, home, faq, settings, feedback

def sidebar():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "Chat", "FAQ / Help"])
    return selection

def main():
    page = sidebar()
    if page == "Home":
        home.display()
    elif page == "Chat":
        chat.display()
    elif page == "FAQ / Help":
        faq.display()

if __name__ == '__main__':
    main()
