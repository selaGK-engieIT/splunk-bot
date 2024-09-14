# splunk-bot
Chatbot for Splunk

app.py is the entry point, and it imports the various pages from the pages/ directory.
Each page (chat, home, FAQ) is in its own script under the pages/ directory.
st.experimental_rerun() is used to refresh the page to show new messages in the chat interface.
