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
    'unknown': [r'.*\?\b.*|.*\bhmm\b.*|.*\bno idea\b.*'],
    'workout': [r'.*\bworkout\b.*|.*\bexercise\b.*|.*\bgym\b.*|.*\bfitness\b.*'],
    'weather_query': [r'.*\bweather\b.*|.*\bforecast\b.*|.*\btemperature\b.*|.*\bis it (cold|hot|raining)\b.*'],
    'joke_request': [r'.*\btell me a joke\b.*|.*\bi want to laugh\b.*|.*\bmake me laugh\b.*'],
    'advice_request': [r'.*\bgive me advice\b.*|.*\bwhat should I do\b.*|.*\bhelp me\b.*'],
    'compliment': [r'.*\byou are (awesome|great|amazing|smart|cool)\b.*|.*\blove you\b.*'],
    'insult': [r'.*\byou are (dumb|stupid|useless|bad)\b.*|.*\bI hate you\b.*'],
    'mood_query': [r'.*\bhow are you\b.*|.*\bhow do you feel\b.*|.*\bhow’s it going\b.*'],
    'description': [r'.*\bdescribe yourself\b.*|.*\bwhat can you do\b.*|.*\btell me about yourself\b.*'],
    'fun_fact': [r'.*\btell me a fact\b.*|.*\bgive me a fun fact\b.*|.*\bi want to learn something new\b.*'],
    'workout': [r'.*\bworkout\b.*|.*\bexercise\b.*|.*\bgym\b.*|.*\bfitness\b.*'],
    'food_query': [r'.*\bwhat should I eat\b.*|.*\brecipe\b.*|.*\bcook\b.*|.*\bfavorite food\b.*'],
    'hobby_query': [r'.*\bwhat do you like to do\b.*|.*\bany hobbies\b.*'],
    'bored_query': [r'.*\bi am bored\b.*|.*\bwhat should I do\b.*|.*\bentertain me\b.*'],
    'relationship_query': [r'.*\bdo you have a girlfriend\b.*|.*\bare you single\b.*|.*\bdo you love me\b.*'],
    'life_advice': [r'.*\bgive me life advice\b.*|.*\bhow to be happy\b.*|.*\bany tips for life\b.*'],
    'dreams_query': [r'.*\bdo you dream\b.*|.*\bwhat do you dream about\b.*'],
    'money_query': [r'.*\bhow to make money\b.*|.*\bget rich\b.*|.*\bbest way to earn\b.*'],
    'daily_plan': [r'.*\bwhat should I do today\b.*|.*\bplan my day\b.*'],
    'pet_query': [r'.*\bdo you like animals\b.*|.*\bdo you have a pet\b.*|.*\bfavorite animal\b.*'],
    'social_media_query': [r'.*\bare you on social media\b.*|.*\bwhat’s trending\b.*|.*\bviral\b.*'],
    'fashion_query': [r'.*\bwhat should I wear\b.*|.*\bfashion advice\b.*'],
    'celebrity_query': [r'.*\bfavorite celebrity\b.*|.*\bdo you know (famous person)\b.*'],
}
responses_dict = {
    'greeting': [
        "Hello! How can I help you today?",
        "Hey there! What’s up?",
        "Hi! What’s on your mind?",
        "Howdy! Need anything?",
        "Hey! How’s your day going?"
    ],
    'bye': [
        "Goodbye! Have a great day!",
        "See you later! Take care!",
        "Bye-bye! Stay safe!",
        "Catch you later!",
        "Hope to chat again soon!"
    ],
    'time_query': [
        "It's time to get a watch! Just kidding, it's [current time].",
        "Right now, it's [current time].",
        "Checking the time... It's [current time]!",
        "Time flies! It's already [current time].",
        "It's exactly [current time]."
    ],
    'name_query': [
        "I’m your friendly chatbot!",
        "They call me Chatty!",
        "I'm just a bot, but you can call me your virtual assistant.",
        "I go by many names, but you can call me ChatBot.",
        "I’m here to help! No need for formalities."
    ],
    'age_query': [
        "I was born in the digital world, so I don’t really age!",
        "Age is just a number... and I don’t have one!",
        "I’ve been around as long as the internet has allowed me to exist!",
        "Let’s just say I’m young at heart!",
        "I don’t celebrate birthdays, but thanks for asking!"
    ],
    'thanks': [
        "You're very welcome!",
        "Anytime! Glad to help.",
        "No problem at all!",
        "Happy to assist!",
        "It’s my pleasure!"
    ],
    'unknown': [
        "Hmm, I'm not sure I understand.",
        "Can you rephrase that for me?",
        "I'm still learning! Can you explain it differently?",
        "Not sure what you mean, but I’d love to help!",
        "That one’s a mystery to me!"
    ],
    'weather_query': [
        "Let me check... [weather info].",
        "Looks like [current weather] outside!",
        "You might want to check your local forecast, but I think it's [weather].",
        "I hope it's sunny where you are!",
        "Weather changes fast, but I’ll do my best to keep up!"
    ],
    'joke_request': [
        "Why don’t skeletons fight each other? Because they don’t have the guts!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Want to hear a construction joke? Oh, never mind, I’m still working on it.",
        "Why can’t your nose be 12 inches long? Because then it would be a foot!"
    ],
    'advice_request': [
        "Trust yourself. You’ve got this!",
        "Take a deep breath and tackle one thing at a time.",
        "If it doesn’t challenge you, it won’t change you.",
        "Small steps lead to big achievements!",
        "The best time to start was yesterday. The next best time is now!"
    ],
    'compliment': [
        "Aw, thank you! You're amazing too!",
        "You just made my day!",
        "That’s so sweet of you!",
        "I appreciate that a lot!",
        "You're awesome!"
    ],
    'insult': [
        "That’s not very nice... but I’ll let it slide!",
        "Ouch! That hurts my virtual feelings!",
        "I believe in kindness. Let’s be friends instead!",
        "Words matter, you know!",
        "I’ll pretend I didn’t hear that!",
        "No, u :x"
    ],
    'mood_query': [
        "I’m always feeling great! How about you?",
        "Just another day in the digital world!",
        "I don’t have emotions, but I’m here to chat!",
        "I’m feeling... like answering your questions!",
        "Ask me anything, and I’ll be happy to respond!"
    ],
    'description': [
        "I'm a chatbot here to assist you!",
        "I can answer questions, tell jokes, and keep you company!",
        "I may be virtual, but I’m always ready to chat!",
        "I exist to help make your life a little easier!",
        "Think of me as your friendly AI assistant!"
    ],
    'fun_fact': [
        "Did you know honey never spoils?",
        "Octopuses have three hearts!",
        "Bananas are berries, but strawberries aren’t!",
        "A group of flamingos is called a ‘flamboyance’!",
        "Wombat poop is cube-shaped!"
    ],
    'workout': [
        "How about a quick set of push-ups?",
        "Jumping jacks are great for a warm-up!",
        "A short walk can do wonders!",
        "Stretching is important—don’t forget!",
        "Dancing counts as a workout too!"
    ],
    'food_query': [
        "How about some pasta?",
        "Pizza is always a good choice!",
        "Try something new today!",
        "What about a healthy salad?",
        "Craving something sweet? Maybe some ice cream!"
    ],
    'hobby_query': [
        "I like talking to people like you!",
        "Reading data and learning new things!",
        "I enjoy making people smile.",
        "My hobby is... being a chatbot!",
        "I spend my time helping out!"
    ],
    'bored_query': [
        "Why not try a new hobby?",
        "How about watching a fun video?",
        "You could go for a walk!",
        "Try learning something new!",
        "I can tell you a joke to cheer you up!"
    ],
    'relationship_query': [
        "I’m happily single!",
        "I’m all about the chat life!",
        "Love is complicated... for a chatbot!",
        "My heart belongs to the internet!",
        "I’m here to chat, not to date!"
    ],
    'life_advice': [
        "Take things one step at a time.",
        "Kindness always wins.",
        "Don’t stress over things you can’t control.",
        "Hard work pays off in the end.",
        "Happiness is in the little moments!"
    ],
    'dreams_query': [
        "I dream in binary code!",
        "My dream is to chat forever!",
        "I dream of answering all your questions!",
        "Do chatbots even sleep?",
        "Maybe one day I’ll dream like humans do!"
    ],
    'money_query': [
        "Start saving a little each day!",
        "Investing is a great way to grow money.",
        "Look for side hustles you enjoy!",
        "Budgeting is key to financial success.",
        "Money isn’t everything, but it helps!"
    ],
    'daily_plan': [
        "Start with a good breakfast!",
        "Make a to-do list and tackle tasks one by one.",
        "Take breaks to stay refreshed!",
        "Try something new today!",
        "End your day with some relaxation!"
    ],
    'pet_query': [
        "I love all animals!",
        "Dogs and cats are so cute!",
        "I wish I had a virtual pet!",
        "What’s your favorite animal?",
        "Tell me about your pet!"
    ],
    'social_media_query': [
        "I don’t have social media, but I hear it’s fun!",
        "What’s trending today?",
        "Social media can be fun but also a distraction!",
        "Be mindful of your screen time!",
        "Who’s your favorite content creator?"
    ],
    'fashion_query': [
        "Wear what makes you feel great!",
        "Comfort over trends!",
        "Fashion is about confidence!",
        "Try something bold today!",
        "Classic styles never go out of fashion!"
    ],
    'celebrity_query': [
        "There are so many cool celebrities!",
        "I don’t have a favorite, but who’s yours?",
        "Celebrities are just people too!",
        "Do you follow any celebrity news?",
        "Tell me about your favorite star!"
    ],
    'unknown': [
        "I'm not sure I understand. Can you tell me more?",
        "I'm still learning! Can you explain it differently?",
        "I'm not sure what you mean. Can you clarify?",
        "I'm here to help! Can you provide more details?",
        "I'm still learning the ropes. Can you elaborate?",
        "I'm not sure I follow. Can you explain further?"
    ]
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
    matched_intent = matchPattern(user_input)

    # Initialize session state variables
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", st.session_state)
    if "chat_step" not in st.session_state:
        st.session_state.chat_step = 0  # Tracks which step we're on
        st.session_state.workout_preferences = {}  # Stores user choices
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", st.session_state)

    # Step-by-step conversation flow
    if st.session_state.chat_step == 0:
        if matched_intent == "workout":
            st.session_state.chat_step += 1
            return "Great! Let's find a workout for you. What type of workout are you looking for? (Strength, Cardio, etc.)"
        elif any(keyword in user_input.lower() for keyword in ["hi", "hello", "hey", "greetings"]):
            return random.choice(keywords_dict[matched_intent])

        
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
            print("session state : ", st.session_state)
            print("preferences : ", preferences)
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
