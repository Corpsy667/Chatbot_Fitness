import random
import pandas as pd
from youtube_functions import search_youtube_video

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

def chatbot():
    # Basic responses for the chatbot
    greetings_responses = ["Hi there!", "Hello!", "Hey! How can I help you today?", "Greetings! Ready to talk fitness?", 'Welcome here', 'Hiii...I am a Bot, how are you?', 'Hey there!', 'Hello!', 'Hi!', 'Hey!', 'Howdy!', 'https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExemw5NWtqN3NhMzVzeHp4cHYxazJ6NXQ0aWk5cWhiMDI5NWMxaGZqNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ASd0Ukj0y3qMM/giphy.gif', 'https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMThiNDgzaW90dnlpcTFpNzF0MXA5cm4wYmV3bDB3d2wwMTk0aXc2MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Cmr1OMJ2FN0B2/giphy.gif']
    thanks_responses = ["You're welcome!", "No problem!", "Anytime!", "Happy to help!"]
    goodbye_responses = ["Goodbye!", "See you later!", "Take care!", "Have a great day!"]
    video_responses = ["Here's a video for you!", "Check out this video!", "Watch this video for more information!", "Here's a small video for you!"]
    # Main loop to interact with the user
    print(random.choice(greetings_responses))
    while True:
        user_input = input("You: ").lower()
        if "workout" in user_input or "exercise" in user_input or "fitness" in user_input or "gym" in user_input or "training" in user_input or "routine" in user_input:
            print("Great! Let's find a workout for you. Please answer a few questions.")
            
            workout_type = input("What type of workout? (e.g., Strength, Cardio, or Any): ").strip()
            while workout_type.lower() not in data["Type"].unique().lower():
                print("please enter a valid workout type such as : Strength, Plyometrics, Cardio, Stretching, Powerlifting, Strongman, Olympic Weightlifting, any")
                workout_type = input("What type of workout? (e.g., Strength, Cardio, or Any): ").strip()
            body_part = input("Which body part do you want to target? (e.g., Abdominals, Legs, or Any): ").strip()
            while body_part.lower() not in data["BodyPart"].unique().lower():
                print("please enter a valid body part such as : Abdominals, Legs, Chest, Back, Shoulders, Arms, Full Body, any")
                body_part = input("Which body part do you want to target? (e.g., Abdominals, Legs, or Any): ").strip()
            equipment = input("Any specific equipment? (e.g., Bands, None, or Any): ").strip()
            while equipment.lower() not in data["Equipment"].unique().lower():
                print("please enter a valid equipment such as : Bands, Dumbbells, Barbell, Kettlebell, None, Any")
                equipment = input("Any specific equipment? (e.g., Bands, None, or Any): ").strip()
            level = input("What difficulty level? (e.g., Beginner, Intermediate, Advanced, or Any): ").strip()
            while level.lower() not in data["Level"].unique().lower():
                print("please enter a valid difficulty level such as : Beginner, Intermediate, Advanced, Any")
                level = input("What difficulty level? (e.g., Beginner, Intermediate, Advanced, or Any): ").strip()
                
            preferences = {
                'Type': workout_type,
                'BodyPart': body_part,
                'Equipment': equipment,
                'Level': level
            }
            
            recommendations = recommend_workout(preferences)
            print("Here are some recommendations:")
            for workout in recommendations:
                title, url = search_youtube_video(workout)
                if title and url:
                    print(f"- {workout}\n{random.choice(video_responses)}: {url}")
                else:
                    print(f"- {workout}, sorry i couldn't find a video for this workout")
        elif any(keyword in user_input for keyword in keywords_dict['greeting']):
            print(random.choice(greetings_responses))
        elif "thank" in user_input or user_input in keywords_dict['thanks']:
            print(random.choice(thanks_responses))
        elif any(keyword in user_input for keyword in keywords_dict['bye']):
            print(random.choice(goodbye_responses))
            break
        else:
            print("I'm not sure I understand. Can you tell me more?")
        
if __name__ == "__main__":
    chatbot()
