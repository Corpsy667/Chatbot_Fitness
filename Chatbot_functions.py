import random
import pandas as pd
from youtube_functions import search_youtube_video
import re
import streamlit as st
from keywords_answers import keywords_dict, responses_dict
# Load the dataset
data = pd.read_csv('megaGymDataset.csv', index_col=0)
data = data.drop(columns=["Rating", "RatingDesc"])

#Lowercase the data for matching
lower_data = data.copy() 
lower_data["Title"] = lower_data["Title"].str.lower()

#function to recommand random workouts with the user preferences
def recommend_workout(preferences, quantity=5):
    """
    Recommend workouts based on user preferences.
    :param preferences: A dictionary with keys like 'Type', 'BodyPart', 'Equipment', and 'Level'.
    :return: A list of recommended workouts.
    """
    filtered_data = data.copy()  # Create a copy of the data to avoid modifying the original

    for key, value in preferences.items():
        if value and value.lower() != "any":
            print(value)
            # Filter where the value matches OR where it's "None"
            filtered_data = filtered_data[filtered_data[key].str.contains(value, case=False, na=False)]
            if value == "Equipment":
                filtered_data = filtered_data[
                    filtered_data[key].str.contains(value, case=False, na=False) |
                    filtered_data[key].str.contains("Body Only", case=False, na=False)
                ]
        else:
            continue

    if filtered_data.empty:
        return ["Sorry, no workouts match your preferences. Try adjusting them!"]
    
    return filtered_data['Title'].sample(n=min(quantity, len(filtered_data))).tolist()  # Return up to 5 random recommendations


def matchPattern(user_msg):
    user_msg = user_msg.lower()
    for intent, patterns in keywords_dict.items():
        for pattern in patterns:
            match = re.search(pattern, user_msg)
            if match:
                return intent
    return 'unknown'

def description(request):
    request = request.lower()
    for pattern in keywords_dict["description"]:
        match = re.match(pattern, request)
        if match:
            sport = match.group(1).strip()
            return sport
    return 'unknown_sport'



def chatbot(user_input):
    url_list = []
    matched_intent = matchPattern(user_input)
    # Initialize session state variables
    if "chat_step" not in st.session_state:
        st.session_state.chat_step = 0  # Tracks which step we're on
        st.session_state.workout_preferences = {}  # Stores user choices

    # Step-by-step conversation flow
    if st.session_state.chat_step == 0:
        if matched_intent == "workout":
            st.session_state.chat_step += 1
            return "Great! Let's find a workout for you. What type of workout are you looking for? (Strength, Cardio, etc.)", url_list
        elif matched_intent == "description":
            sport = description(user_input)
            if sport != 'unfound_desc':
                sport_desc = lower_data.loc[lower_data["Title"] == sport, "Desc"]
                if sport_desc.empty or pd.isna(sport_desc.values):
                    return random.choice(responses_dict["unfound_desc"]), url_list
                else:
                    return sport_desc.values[0], url_list
            else: 
                return random.choice(responses_dict["unknown_sport"]), url_list
        
        else:
            return random.choice(responses_dict[matched_intent]), url_list

    elif st.session_state.chat_step == 1:
        user_input = st.session_state.messages[-1]["content"]
        types_lower = [str(x).lower() for x in data["Type"].unique()]
        if user_input.title().lower() in types_lower or user_input.title().lower() == "any":
            st.session_state.workout_preferences["Type"] = user_input.title()
            st.session_state.chat_step += 1
            return "Which body part do you want to target? (Abdominals, Biceps, Chest, Any etc.)", url_list
        else:
            return "Please enter a valid workout type: Strength, Plyometrics, Cardio, Stretching, Powerlifting, Strongman, Olympic Weightlifting, Any", url_list

    elif st.session_state.chat_step == 2:
        user_input = st.session_state.messages[-1]["content"]
        bodyp_lower = [str(x).lower() for x in data["BodyPart"].unique()]
        if user_input.title().lower() in bodyp_lower or user_input.title().lower() == "any":
            st.session_state.workout_preferences["BodyPart"] = user_input.title()
            st.session_state.chat_step += 1
            return "Any specific equipment? (Bands, Dumbbell, Barbell, Bands, Body Only, Any, etc.)", url_list
        else:
            return "Please enter a valid body part: Abdominals, Adductors, Abductors, Biceps, Calves, Chest, Forearms, Glutes, Hamstrings, Lats, Lower Back, Middle Back, Traps, Neck, Quadriceps, Shoulders, Triceps, Any", url_list

    elif st.session_state.chat_step == 3:
        user_input = st.session_state.messages[-1]["content"]
        equip_lower = [str(x).lower() for x in data["Equipment"].unique()]
        if user_input.title().lower() in equip_lower or user_input.title().lower() == "any":
            st.session_state.workout_preferences["Equipment"] = user_input.title()
            st.session_state.chat_step += 1
            return "What difficulty level? (Beginner, Intermediate, Expert, Any)", url_list
        else:
            return "Please enter a valid equipment type: Bands, Barbell, Kettlebells, Dumbbell, Other, Cable, Machine, Body Only, Medicine Ball, Exercise Ball, Foam Roll, E-Z Curl Bar, Any", url_list

    elif st.session_state.chat_step == 4:
        user_input = st.session_state.messages[-1]["content"]
        level_lower = [str(x).lower() for x in data["Level"].unique()]
        if user_input.title().lower() in level_lower or user_input.title().lower() == "any":
            st.session_state.workout_preferences["Level"] = user_input.title()
            st.session_state.chat_step += 1

            # Now that we have all inputs, generate recommendations
            preferences = st.session_state.workout_preferences
            recommendations = recommend_workout(preferences)
            if recommendations == ["Sorry, no workouts match your preferences. Try adjusting them!"]:
                response = recommendations[0]
            else:
                response = "Here are some recommended workouts:\n"
                for workout in recommendations:
                    title, url = search_youtube_video(workout)
                    if title and url:
                        response += f"- {workout}\n"
                        url_list.append(url)
                    else:
                        response += f"- {workout}, but no video found.\n"

            # Reset state after providing recommendations
            st.session_state.chat_step = 0
            st.session_state.workout_preferences = {}
            response += {random.choice(responses_dict["video"])}
            return response, url_list

        else:
            return "Please enter a valid difficulty level: Beginner, Intermediate, Expert, Any.", url_list