#Rule based AI Chat bot

import datetime
import time

name=input("Welcome, Enter your name: ")
presentHour=datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good morning, ",name) 
elif 11 <= presentHour <= 17:
    print("Good afternoon, ",name)
elif 17 <= presentHour <= 20:
    print("Good evening, ",name)
else:
    print("Good night, ",name)


print("Namaste! Welcome to LOVE chatbot")
print("You can ask me basic question and do some basic work which i can do,Type 'bye' to exit from the bot")

#Chat bot Memory Creation [ dictionary of responses]

responses={
    "hello":"Hi,Welcome. How can I help you?",
    "hi":"hello",
    "how are you":"I am fine. Thank you",
    "who are you":"I am smart LOVE chatbot",
    "what is python":"Python is a popular programming language.",
    "what can you do": "I can answer questions, tell the time, "
            "and perform simple tasks.",
    "listen music":
        "Opening Spotify for you 🎵",
    "videos":"Open YOUTUBE",
    "calculate":"open calculator"
    
}


#Method /Function to get response to chat bot

def getResponseOfBot(userquestion):
    userquestion=userquestion.lower()
    for eachkey in responses:
        if eachkey in userquestion:
            return responses[eachkey]

    return "Ask Google or chat gpt"
  

#Take user Input
while True:
    userInput=input("Please ask your question: ")
    reply=getResponseOfBot(userInput)
    print("Bot Response:",reply)

    if "bye" in userInput.lower():
        break




