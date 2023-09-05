import streamlit as st
import json
import requests
import os

def load_chat_history(filename="chat_history.json"):
    """Load previous chat history from a JSON file."""
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return {}

def save_chat_history(history, filename="chat_history.json"):
    """Save the chat history into a JSON file."""
    with open(filename, "w") as f:
        json.dump(history, f)

def handle_user_input(user_input):
    """Handle the user input and get the bot's response."""
    # Generate a new chat name if it's a new chat
    if st.session_state['chat_name'] == "New Chat":
        url = "http://127.0.0.1:8001/conversation/get_name"
        response = requests.post(f"{url}?query={user_input}")
        if response.status_code == 200:
            st.session_state['chat_name'] = response.json()
    
    # Prepare data for POST request
    url = "http://127.0.0.1:8001/chatDB/query_database"
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    payload = {
        "prompt": user_input,
        "chat_history": json.dumps(st.session_state['chat_history'])
    }

    # Make POST request and handle response
    with st.spinner("Bot is typing..."):
        response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        bot_response = response.json()
        st.session_state.chat_history.append({"name": "assistant", "message": bot_response})
        
    else:
        st.session_state.chat_history.append({"name": "assistant", "message": f"An error occurred. Status code: {response.status_code}"})
        bot_response = f"An error occurred. Status code: {response.status_code}"
    with st.chat_message("assistant"):
        st.write(bot_response)
# Initialize
chat_history_dict = load_chat_history()

# Streamlit session state
if 'chat_name' not in st.session_state:
    st.session_state['chat_name'] = "New Chat"
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# UI Elements
st.title("Chat with your personal data")

# Sidebar for chat history
st.sidebar.header("Previous Chats")
for chat_name in chat_history_dict.keys():
    if st.sidebar.button(chat_name):
        st.session_state['chat_name'] = chat_name
        st.session_state['chat_history'] = chat_history_dict[chat_name]

# Main chat window
user_input = st.chat_input("You: ")
if user_input:
    st.session_state.chat_history.append({"name": "user", "message": user_input})
# Developer Info
st.sidebar.markdown("Developed by `Sagar Dollin`", unsafe_allow_html=True)
# Display chat history
# st.write(f"Chat: {st.session_state['chat_name']}")
for chat in st.session_state.chat_history:
    with st.chat_message(chat["name"]):
        st.write(chat["message"])

if user_input:
    handle_user_input(user_input)
    chat_history_dict[st.session_state['chat_name']] = st.session_state['chat_history']
    save_chat_history(chat_history_dict)



