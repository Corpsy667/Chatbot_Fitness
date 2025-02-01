import random
import pandas as pd
from youtube_functions import search_youtube_video
import re
import streamlit as st
# Load the dataset
data = pd.read_csv('megaGymDataset.csv', index_col=0)
data = data.drop(columns=["Rating", "RatingDesc"])

def recommend_workout(preferences):
    """
    Recommend workouts based on user preferences.
    :param preferences: A dictionary with keys like 'Type', 'BodyPart', 'Equipment', and 'Level'.
    :return: A list of recommended workouts.
    """
    filtered_data = data
    for key, value in preferences.items():
        if value and value.lower() != "any":
            filtered_data = filtered_data[filtered_data[key].str.contains(value, case=False, na=False)]
    
    if filtered_data.empty:
        return ["Sorry, no workouts match your preferences. Try adjusting them!"]
    
    return filtered_data['Title'].sample(n=min(5, len(filtered_data))).tolist()  # Return up to 5 random recommendations

keywords_dict = {
    'greeting': [r'.*\bhell+o+\b.*|.*\bhi+\b.*|.*\bho+w+dy\b.*|.*\bhul+lo+\b.*|.*\bhey\b.*|.*\bho+l+a+\b.*'],
    'bye': [r'.*\bby+e+\b.*|.*\bgoo+db+ye\b.*|.*\bsee you\b.*|.*\btake care\b.*|.*\bcy+a+\b.*|.*have a great (night|da+y+).*'],
    'time_query': [r'.*\btime\b.*|.*clock\b.*|.*what time is it.*|.*tell me the time.*|.*do you have the time.*'],
    'name_query': [r'.*\byour name\b.*|.*who are you\b.*|.*what is your name\b.*'],
    'age_query': [r'.*\bhow old are you\b.*|.*\bwhat is your age\b.*|.*\bwhen were you born\b.*|.*\bage.*\b.*'],
    'thanks': [r'.*\bthank you\b.*|.*\bthanks\b.*|.*\bappreciate\b.*|.*\bgrateful\b.*'],
    'weather': [r'\b(weather|forecast)(?: in (?P<city>\w+))?(?: for (?P<time>today|tomorrow))?\b'],
    'unknown': [r'.*\?\b.*|.*\bhmm\b.*|.*\bno idea\b.*']
}
def matchPattern(user_msg):
    user_msg = user_msg.lower()
    for intent, patterns in keywords_dict.items():
        for pattern in patterns:
            match = re.search(pattern, user_msg)
            if match:
                return intent
    return 'unknown'

def chatbot(user_input):
    greetings_responses = ["Hi there!", "Hello!", "Hey! How can I help you today?", "Greetings! Ready to talk fitness?", "Welcome here!", "Hiii... I am a Bot, how are you?", "Hey there!", "Howdy!"]
    thanks_responses = ["You're welcome!", "No problem!", "Anytime!", "Happy to help!", "You're welcome! Let me know if you need anything else!"]
    goodbye_responses = ["Goodbye!", "See you later!", "Take care!", "Have a great day!"]
    video_responses = ["Here's a video for you!", "Check out this video!", "Watch this video for more information!"]

def chatbot(user_input):
    greetings_responses = ["Hi there!", "Hello!", "Hey! How can I help you today?", "Greetings! Ready to talk fitness?", "Welcome here!", "Hiii... I am a Bot, how are you?", "Hey there!", "Howdy!"]
    thanks_responses = ["You're welcome!", "No problem!", "Anytime!", "Happy to help!", "You're welcome! Let me know if you need anything else!"]
    goodbye_responses = ["Goodbye!", "See you later!", "Take care!", "Have a great day!"]
    video_responses = ["Here's a video for you!", "Check out this video!", "Watch this video for more information!"]

    # Initialize session state variables
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", st.session_state)
    if "chat_step" not in st.session_state:
        st.session_state.chat_step = 0  # Tracks which step we're on
        st.session_state.workout_preferences = {}  # Stores user choices
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", st.session_state)

    # Step-by-step conversation flow
    if st.session_state.chat_step == 0:
        if any(keyword in user_input.lower() for keyword in ["workout", "exercise", "fitness"]):
            st.session_state.chat_step += 1
            return "Great! Let's find a workout for you. What type of workout are you looking for? (Strength, Cardio, etc.)"
        elif any(keyword in user_input.lower() for keyword in ["hi", "hello", "hey", "greetings"]):
            return random.choice(greetings_responses)
        
        elif any(keyword in user_input.lower() for keyword in ["thank", "thanks"]):
            return random.choice(thanks_responses)
        
        elif any(keyword in user_input.lower() for keyword in ["bye", "goodbye", "see you", "take care"]):
            return random.choice(goodbye_responses)
        
        else:
            return "I'm not sure I understand. Can you tell me more?"

    elif st.session_state.chat_step == 1:
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", st.session_state)
        user_input = st.session_state.messages[-1]["content"]
        if user_input.title() in data["Type"].unique():
            st.session_state.workout_preferences["Type"] = user_input.title()
            st.session_state.chat_step += 1
            return "Which body part do you want to target? (Abdominals, Legs, etc.)"
        else:
            return "Please enter a valid workout type: Strength, Cardio, Plyometrics, etc."

    elif st.session_state.chat_step == 2:
        user_input = st.session_state.messages[-1]["content"]
        if user_input.title() in data["BodyPart"].unique():
            st.session_state.workout_preferences["BodyPart"] = user_input.title()
            st.session_state.chat_step += 1
            return "Any specific equipment? (None, Dumbbells, Barbells, etc.)"
        else:
            return "Please enter a valid body part: Abdominals, Legs, Chest, etc."

    elif st.session_state.chat_step == 3:
        user_input = st.session_state.messages[-1]["content"]
        if user_input.title() in data["Equipment"].unique():
            st.session_state.workout_preferences["Equipment"] = user_input.title()
            st.session_state.chat_step += 1
            return "What difficulty level? (Beginner, Intermediate, Advanced, Any)"
        else:
            return "Please enter a valid equipment type: None, Dumbbells, Barbells, etc."

    elif st.session_state.chat_step == 4:
        user_input = st.session_state.messages[-1]["content"]
        if user_input.title() in data["Level"].unique():
            st.session_state.workout_preferences["Level"] = user_input.title()
            st.session_state.chat_step += 1

            # Now that we have all inputs, generate recommendations
            preferences = st.session_state.workout_preferences
            recommendations = recommend_workout(preferences)

            response = "Here are some recommended workouts:\n"
            for workout in recommendations:
                title, url = "test", "abc" #search_youtube_video(workout)
                if title and url:
                    response += f"- {workout}\nHere's a video: {url}\n"
                else:
                    response += f"- {workout}, but no video found.\n"

            # Reset state after providing recommendations
            st.session_state.chat_step = 0
            st.session_state.workout_preferences = {}

            return response

        else:
            return "Please enter a valid difficulty level: Beginner, Intermediate, Advanced, Any."


        
if __name__ == "__main__":
    chatbot()
