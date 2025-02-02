
keywords_dict = {
    'greeting': [r'.*\bhell+o+\b.*|.*\bhi+\b.*|.*\bho+w+dy\b.*|.*\bhul+lo+\b.*|.*\bhey\b.*|.*\bho+l+a+\b.*'],
    'bye': [r'.*\bby+e+\b.*|.*\bgoo+db+ye\b.*|.*\bsee you\b.*|.*\btake care\b.*|.*\bcy+a+\b.*|.*have a great (night|da+y+).*'],
    'time_query': [r'.*\btime\b.*|.*clock\b.*|.*what time is it.*|.*tell me the time.*|.*do you have the time.*'],
    'name_query': [r'.*\byour name\b.*|.*who are you\b.*|.*what is your name\b.*'],
    'age_query': [r'.*\bhow old are you\b.*|.*\bwhat is your age\b.*|.*\bwhen were you born\b.*|.*\bage.*\b.*'],
    'thanks': [r'.*\bthank you\b.*|.*\bthanks\b.*|.*\bappreciate\b.*|.*\bgrateful\b.*|.*\bok\b.*'],
    'unknown': [r'.*\?\b.*|.*\bhmm\b.*|.*\bno idea\b.*'],
    'workout': [r'.*\bworkout\b.*|.*\bexercise\b.*|.*\bgym\b.*|.*\bfitness\b.*|.*\btraining\b.*|.*\bphysical activity\b.|.*\bwrokout\b.*|.*\bworout\b.*|.*\bworkut\b.*'],
    'weather_query': [r'.*\bweather\b.*|.*\bforecast\b.*|.*\btemperature\b.*|.*\bis it (cold|hot|raining)\b.*'],
    'joke_request': [r'.*\bjoke\b.*|.*\bi want to laugh\b.*|.*\bmake me laugh\b.*'],
    'advice_request': [r'.*\bgive me advice\b.*|.*\bwhat should I do\b.*|.*\bhelp me\b.*'],
    'compliment': [r'.*\byou are (awesome|great|amazing|smart|cool)\b.*|.*\blove you\b.*'],
    'insult': [r'.*\byou are (dumb|stupid|useless|bad)\b.*|.*\bI hate you\b.*'],
    'mood_query': [r'.*\bhow are you\b.*|.*\bhow do you feel\b.*|.*\bhow’s it going\b.*'],
    "description": [r'.*\b(?:describe me|what is|tell me more about) (.+)'],
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
    'fashion_query': [r'.*\bwhat should i wear\b.*|.*\bfashion advice\b.*'],
    'celebrity_query': [r'.*\bfavorite celebrity\b.*'],
    'agreement_query': [r'.*\bi agree\b.*|.*\bi think so\b.*|.*\bi believe\b.*'],
    'Quoi': [r'.*\bquoi\b.*|.*wait what.*'],
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
        "It's time to get a watch!",
        "Right now, it's .. Nah idk don't have this part implemented",
        "Checking the time... U're gonna wait forever to get the answer",
        "Time flies!",
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
        "It’s my pleasure!",
        "I'm the GOAT :D"
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
    'video' : [
        "Here's a video for you!", 
        "Check out this video!", 
        "Watch this video for more information!",
        "I found a video for you!",
        "This video might help!",
        "Here's a video that might interest you!",
        "If you're too dumb to know what it is, watch this video!"],
    'unknown': [
        "I'm not sure I understand. Can you tell me more?",
        "I'm still learning! Can you explain it differently?",
        "I'm not sure what you mean. Can you clarify?",
        "I'm here to help! Can you provide more details?",
        "I'm still learning the ropes. Can you elaborate?",
        "I'm not sure I follow. Can you explain further?",
        "Uh ?",
        "Ok i guess",
        "Nahhhh"
    ],
    'agreement_query': [
        "Of course you agree did you think I was wrong?",
        "I'm always right",
        "You're smart",
        "Never doubt me you dirty b*tch. Sorry i forgot i couldn't swear here",
        "I know..."
    ],
    'Quoi': ["Feur"],
    'unfound_desc': [
        "I know the sport, but I don't have a description for it. Would you like a workout recommendation instead?",
        "Sorry.. bip bip error.. Sport found but not the description",
        "I can't find the description for this sport. Would you like a workout recommendation instead?",
        "This sport is still in workout, try another one",
        "You don't have the level for this exercise pick something else",
        "Could not find the sport you are refering to in my database. You can blame the devellopers"
        ],
    'unknown_sport': [
        "Can't you be normal and ask for a sport that exists?",
        "How about you give me a normal sport name?",
        "I'm not sure what that is. Can you try again with a different sport name?",
        "I'm not familiar with that sport. Can you try another one?",
        "Bro, you're asking for sports that don't exist. Try again with a real sport name.",
        "I'm done with you. Ask for a real sport.",
        "Error in your brain - sport not found."]

}