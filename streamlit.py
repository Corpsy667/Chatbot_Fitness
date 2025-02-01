import streamlit as st
from Chatbot_functions import *

import streamlit as st
import pandas as pd


# Function to ask questions and suggest workout
def suggest_workout(user_input):
    if any(keyword in user_input.lower() for keyword in ['workout', 'exercise', 'fitness']):
        st.write("What type of workout are you looking for?")
        workout_type = st.selectbox("Select Workout Type", workouts_df['workout_type'].unique())
        
        # Filter workouts based on user selection
        selected_workout = workouts_df[workouts_df['workout_type'] == workout_type]
        
        # Ask additional questions if needed (for example, difficulty)
        difficulty = st.selectbox("Select Difficulty", selected_workout['difficulty'].unique())
        filtered_workout = selected_workout[selected_workout['difficulty'] == difficulty]

        # Display results
        st.write(f"Based on your choice, I recommend: {filtered_workout['workout_type'].values[0]}")
        st.write(f"Duration: {filtered_workout['duration'].values[0]}")
        st.write(f"Equipment needed: {filtered_workout['equipment'].values[0]}")
    else:
        st.write("Can you please tell me what you're looking for in terms of exercise or workout?")

# Streamlit user interface

st.title("Workout Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

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
            response = chatbot(prompt)
            message = {"role": "assistant", "content": response}
            st.write(response) 
    st.session_state.messages.append(message)