This is chatbot project for gym workout

You will need to create a project on console.cloud.google and go on Youtube Data API v3 and create your own key
After you created your key, you can create a python file named "Api_key.py" and enter your youtube api key : YOUTUBE_API_KEY = '**YOUR_KEY**'

You need to download the requirements with : pip install -r requirements.txt

Chatbot_function regroups the functions about the chatbot

Streamlit.py is the application you need to run.
You can run it with **streamlit run streamlit.py** in your terminal
It basically contains the chatbot

youtube_functions is the file to withdraw youtube information so you can display a youtube video on streamlit

megaGymDataset.csv is a dataset we found on kaggle.com but you can replace it with whatever you want don't forget to preprocess the data so it works with the chatbot "Desc" column for description, "Title" for the name of the workout, "Equipment", for the needed equipment, "Type" for the part of the body you want to train, "Level" for the level you want to train for rating has been dropped since we didn't know what to do with that and ratingdesc same.

Note that there are some none values in the description because not every description was existing in the dataset from kaggle.

keywords_answers are the answers and the chat we thought of but you can replace or add anything you want in it