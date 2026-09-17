# Rule based AI Chat bot

import datetime
import time
import webbrowser
from urllib.parse import quote


# Take user's name
name = input("Welcome, Enter your name: ")

presentHour = datetime.datetime.now().hour

if 5 <= presentHour < 12:
    print("Good morning,", name)
elif 12 <= presentHour < 17:
    print("Good afternoon,", name)
elif 17 <= presentHour < 21:
    print("Good evening,", name)
else:
    print("Good night,", name)


print("Namaste! Welcome to LOVE chatbot")
print("You can ask me basic questions and perform simple tasks.")
print("Type 'bye' to exit from the bot")


# Chatbot Memory Creation [dictionary of responses]

responses = {
    "hello": "Hi, Welcome. How can I help you?",
    "hi": "Hello! Welcome to LOVE chatbot.",
    "hey": "Hey! How can I help you?",
    "how are you": "I am fine. Thank you!",
    "who are you": "I am the smart LOVE chatbot.",
    "what is python": "Python is a popular programming language.",
    "what can you do": "I can answer questions and perform simple tasks.",
    "listen music": "Opening Spotify for you ",
    "videos": "Opening YouTube for you ",
    "for querry":"open GOOGLE",
    "calculate":"open calculator"
}



# SPOTIFY FUNCTION


def open_spotify():
    print("LOVE Bot: Opening Spotify 🎵")
    webbrowser.open_new_tab("https://open.spotify.com/")


# YOUTUBE FUNCTION


def open_youtube():
    print("LOVE Bot: Opening YouTube ▶️")
    webbrowser.open_new_tab("https://www.youtube.com/")



# GOOGLE FUNCTION


def open_google():
    print("LOVE Bot: Opening Google 🔍")
    webbrowser.open_new_tab("https://www.google.com/")



# CHATGPT FUNCTION


def open_chatgpt():
    print("LOVE Bot: Opening ChatGPT 🤖")
    webbrowser.open_new_tab("https://chatgpt.com/")



# DATE AND TIME FUNCTIONS

def show_date():
    today = datetime.datetime.now().strftime("%d-%m-%Y")
    return "Today's date is " + today


def show_time():
    current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
    return "The current time is " + current_time

# GOOGLE SEARCH FUNCTION


def google_search(query):
    search_url = "https://www.google.com/search?q=" + quote(query)
    webbrowser.open_new_tab(search_url)


# CALCULATOR FUNCTION


def calculator():
    try:
        number1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        number2 = float(input("Enter second number: "))

        if operator == "+":
            result = number1 + number2
        elif operator == "-":
            result = number1 - number2
        elif operator == "*":
            result = number1 * number2
        elif operator == "/":
            if number2 == 0:
                return "Cannot divide by zero."
            result = number1 / number2
        else:
            return "Invalid operator."

        return "The result is " + str(result)

    except ValueError:
        return "Please enter valid numbers."



# FUNCTION TO GET BOT RESPONSE


def getResponseOfBot(userquestion):

    userquestion = userquestion.lower().strip()

    # Exit command
    if userquestion == "bye":
        return "Goodbye! Have a nice day!"

    # Spotify command
    if (
        "listen music" in userquestion
        or "play music" in userquestion
        or "open spotify" in userquestion
    ):
        open_spotify()
        return "Opening Spotify for you 🎵"

    # YouTube command
    if "open youtube" in userquestion or "watch videos" in userquestion:
        open_youtube()
        return "Opening YouTube for you ▶️"

    # Google command
    if userquestion == "open google":
        open_google()
        return "Opening Google for you 🔍"

    # ChatGPT command
    if userquestion == "open chatgpt":
        open_chatgpt()
        return "Opening ChatGPT for you 🤖"

    # Date command
    if "what is the date" in userquestion or userquestion == "date":
        return show_date()

    # Time command
    if "what is the time" in userquestion or userquestion == "time":
        return show_time()

    # Calculator command
    if userquestion == "calculator" or userquestion == "calculate":
        return calculator()

    # Google search command
    if userquestion.startswith("search "):
        query = userquestion[7:]
        google_search(query)
        return "Searching Google for " + query

    # Search for a response in the dictionary
    for eachkey in responses:
        if eachkey in userquestion:
            return responses[eachkey]

    # Default response
    return "Sorry, I don't understand that question."



# MAIN CHATBOT 

while True:

    userInput = input("\nPlease ask your question: ")

    reply = getResponseOfBot(userInput)

    print("Bot Response:", reply)

    if userInput.lower().strip() == "bye":
        break