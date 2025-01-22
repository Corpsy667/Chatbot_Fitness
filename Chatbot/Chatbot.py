import random
import pandas as pd

# Load the dataset
print("cc")
data = pd.read_csv('megaGymDataset.csv')

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

def chatbot():
    # Basic responses for the chatbot
    greetings = ["Hi there!", "Hello!", "Hey! How can I help you today?", "Greetings! Ready to talk fitness?"]
    thanks_responses = ["You're welcome!", "No problem!", "Anytime!", "Happy to help!"]
    goodbye_responses = ["Goodbye!", "See you later!", "Take care!", "Have a great day!"]

    # Main loop to interact with the user
    print(random.choice(greetings))
    while True:
        user_input = input("You: ").lower()

        if any(keyword in user_input for keyword in ["hi", "hello", "hey"]):
            print(random.choice(greetings))
        elif "thank" in user_input:
            print(random.choice(thanks_responses))
        elif any(keyword in user_input for keyword in ["bye", "goodbye", "see you"]):
            print(random.choice(goodbye_responses))
            break
        elif "workout" in user_input:
            print("Great! Let's find a workout for you. Please answer a few questions.")
            
            workout_type = input("What type of workout? (e.g., Strength, Cardio, or Any): ").strip()
            body_part = input("Which body part do you want to target? (e.g., Abdominals, Legs, or Any): ").strip()
            equipment = input("Any specific equipment? (e.g., Bands, None, or Any): ").strip()
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
                print(f"- {workout}")
        else:
            print("I'm not sure I understand. Can you tell me more?")

if __name__ == "__main__":
    chatbot()
