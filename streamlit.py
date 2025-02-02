import streamlit as st
from Chatbot_functions import *

import streamlit as st
import pandas as pd


# Streamlit user interface

st.title("Workout Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []
    message = {"role": "assistant", "content": "Hello! I'm your chatbot assistant. How can I help you today?"}
    st.session_state.messages.append(message)

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# React to user input
if prompt := st.chat_input("Say something..." ):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Get chatbot response
# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response, url_liste = chatbot(prompt)
            message = {"role": "assistant", "content": response}
            st.write(response)
            for url in url_liste:
                st.video(url)
    st.session_state.messages.append(message)