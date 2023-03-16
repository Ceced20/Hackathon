import random
import re
import requests
import nltk
from nltk.chat.util import Chat, reflections
from nltk.corpus import wordnet

# Define the chatbot patterns and responses
patterns = [
    (r'hi|hello|hey.*', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you.*', ['I am doing well, thank you!', 'I am fine, thank you for asking.']),
    (r'what\'s your name.*|who are you.*', ['My name is Chatbot.', 'You can call me Chatbot.']),
    (r'synonym for (.*)', ['Here are some synonyms for {}: {}.', 'Some synonyms for {} are: {}.']),
    (r'antonym for (.*)', ['Here are some antonyms for {}: {}.', 'Some antonyms for {} are: {}.']),
    (r'what is the weather in (.*)', []),
    (r'who made you.*', ['I was made by ceced.']),
    (r'quit.*', ['Bye!', 'Goodbye!']),
]

# Define a function to handle the pattern matching
def match_pattern(patterns, message):
    for pattern, responses in patterns:
        match = re.search(pattern, message, re.IGNORECASE)
        if match:
            if "weather" in pattern:
                city = match.group(1)
                weather = get_weather(city)
                if weather:
                    return "The weather in {} is {} with a temperature of {}°C.".format(city, weather["description"], round(weather["temp"]))
                else:
                    return "Sorry, I could not find the weather for {}.".format(city)
            else:
                response = random.choice(responses)
                if '{}' in response:
                    word = match.group(1)
                    synonyms = []
                    antonyms = []
                    for syn in wordnet.synsets(word):
                        for lemma in syn.lemmas():
                            synonyms.append(lemma.name())
                            if lemma.antonyms():
                                antonyms.append(lemma.antonyms()[0].name())
                    if "synonym" in pattern:
                        response = response.format(word, ", ".join(set(synonyms)))
                    elif "antonym" in pattern:
                        response = response.format(word, ", ".join(set(antonyms)))
                return response

# Define a function to get the weather for a city using the OpenWeatherMap API
def get_weather(city):
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        "q": city,
        "units": "metric",
        "appid": "a1bd9468bd6077d6a261f6c1530dbb37"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = {
            "temp": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
        return weather
    else:
        return None

# Create a Chat object and start chatting
def chat():
    print("Hello, I'm a CygnusChat!")
    print("Ask me anything, or type 'quit' to exit.")
    chatbot = Chat(patterns, reflections)
    while True:
        message = input("You: ")
        if message.lower() == 'quit':
            break
        response = match_pattern(patterns, message)
        if response:
            print("CygnusChat: ", response)
        else:
            print("CygnusChat: ", chatbot.respond(message))

if __name__ == "__main__":
    nltk.download('wordnet')
    chat()
