########</Developed by @realdarkstar>########

## Feel free to contribute to this project ##

# from email.message import EmailMessage
import webbrowser
import pyttsx3
import pywhatkit
import speech_recognition as sr
from datetime import datetime
from decouple import config
from random import choice
import requests
import wikipedia
import os
import subprocess as sp
import os_ops
import smtplib

USERNAME = config("USER")
BOTNAME = config("BOT")

EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")

NEWS_API_KEY = config("NEWS_API_KEY")

OPEN_WEATHER_APPID = config("OPEN_WEATHER_APPID")

TMDB_API_KEY = config("TMDB_API_KEY")


# Text to Speech engine used in this code, helps us to take text input from user and convert it to speech
engine = pyttsx3.init('sapi5')

# Setting the values like volume based on the pyttsx3 module using setProperty method 
engine.setProperty('rate', 190)
engine.setProperty('volume', 1.0)

# Fetching the voices provided by the module pyttsx3(has only 2 voices stored in the module by default) using getProperty method
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    '''Speak function will help our AI to be able to speak using pyttsx3 module'''
    engine.say(audio)
    engine.runAndWait()

def greet_user():
    '''Greet function will be used to allow AI to greet the user'''
    hour = datetime.now().hour
    if (hour >= 0) and (hour < 12):
        speak(f"Good Morning sir {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good AfterNoon sir {USERNAME}")
    elif (hour >= 16) and (hour < 21):
        speak(f"Good Evening sir {USERNAME}")
    speak(f"I'm {BOTNAME}. How may i assist you ?")

def take_user_input():
    '''This function will help AI to take inputs from the user'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"listening........")
        r.pause_threshold = 1
        audio = r.listen(source)
    '''We've used try and except as this part of the code will may throw a error because of many reasons like 
    the invalid input from the user'''
    try:
        print(f"Recognizing......")
        query = r.recognize_google(audio, language='en-uk')
        opening_text = [
        "Cool, I'm on it!", 
        "Got that, wait a few seconds.", 
        "Lightening Speed sir., wait a second.", 
        "Working on it sir. "
    ]
        print(query)
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if (hour >= 22) and (hour < 6):
                speak(f"Good Evening sir, See You Later.")
            else:
                speak(f"Good Bye sir, see you tomorrow.")
            exit()
    except Exception as e:
        print(e)
        speak('Sorry sir, I could not understand that, Could you please say that again ?')
        query = 'None'
    return query

def whatsapp_msg(number, message):
    '''We have used pywhatkit module to use the sendwhatmsg_instantly function in it.'''
    op_whatsapp = pywhatkit.sendwhatmsg_instantly(f"+91{int(number)}", message)
    return op_whatsapp

def send_email(receiver_address, subject, message):
    '''send_email function helps us to send email to any valid email address using smtplib module'''
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(receiver_address, subject, message)
        server.close()
        return True

    except Exception as e:
        print(e)
        return False

def get_latest_news():
    news_dict = []
    result = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = result["articles"]
    for article in articles:
        news_dict.append(article["title"])
    return news_dict[:5]

def get_weather_report(city):
    result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Delhi,IN&APPID={OPEN_WEATHER_APPID}").json()
    weather = result["weather"][0]["main"]
    temperature = result["main"]["temp"]
    feels_like = result["main"]["feels_like"]
    return weather, f"{temperature}℃" f"{feels_like}℃"

def get_trending_movies():
    movies = []
    result = requests.get(f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    res = result["results"]
    for movie in res:
        movies.append(movie["original_title"])
    return movies[:5]

def get_jokes():
    headers = {
            'Accept': 'application/json'
    }
    result = requests.get(f"https://icanhazdadjoke.com/", headers=headers).json()
    return result["joke"]

def get_random_advice():
    result = requests.get(f"https://api.adviceslip.com/advice").json()
    return result["slip"]["advice"]

if __name__=="__main__":
    greet_user()

    while True:
        query = take_user_input().lower()

        if 'open code' in query:
            result = os.startfile(os_ops.paths['vs code'])

        elif 'open calculator' in query:
            sp.Popen(os_ops.paths['calculator'])

        elif 'open notepad' in query:
            os.startfile(os_ops.paths['notepad'])
        
        elif 'open putty' in query:
            os.startfile(os_ops.paths['putty'])

        elif 'open brave' in query:
            os.startfile(os_ops.paths['brave'])

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'my ip' in query:
            result = requests.get('https://api64.ipify.org?format=json').json()
            print(result["ip"])
            speak(f"Your IP address is {result}")

        elif 'on wikipedia' in query:
            speak("searching wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'on google' in query:
            speak("searching....")
            query = query.replace("search", "")
            query = query.replace("on google", "")
            pywhatkit.search(query)

        elif 'on youtube' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            query = query.replace("on youtube", "")
            pywhatkit.playonyt(query)

        elif 'send a whatsapp message' in query:
            print("Please Wait.....")
            speak("Please enter the number you want to text sir.")
            number = input("Enter the number you want to text => ")
            speak("What should be the message you want to send sir ?")
            message = take_user_input().lower()
            whatsapp_msg(number, message)
            speak("Message sent !")

        elif 'send an email' in query:
            speak("Enter the receiver's address, good sir ?")
            receiver_address = input("Enter the receiver's address here => ")
            speak("What should be the subject, sir ?")
            subject = take_user_input().capitalize()
            speak("what should i say in the message sir ?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):                
                speak("Email has been sent !")
            else:
                speak("Something went wrong while sending the email, please try again with the correct details.")

        elif 'news headlines' in query:
            speak("please wait.....")
            result = get_latest_news()
            print(result, sep="\n")
            speak(result)

        elif 'weather today' in query:
            speak("Wait a second")
            my_ip = requests.get('https://api64.ipify.org?format=json').json()
            ip = my_ip["ip"]
            city = requests.get(f"https://ipapi.co/{ip}/city/").text()
            weather, temperature, feels_like = get_weather_report(city)
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
            speak(f"The weather will be {weather} in your city. The Temperature will be {temperature} and it feels_like {feels_like} in your city.")

        elif 'trending movies' in query:
            speak("Please Wait.....")
            speak("There you go, sir")
            speak(f"Top Trending movies now are : {get_trending_movies()}")
            print(get_trending_movies(), sep="\n")

        elif 'tell me a joke' in query:
            speak("Wait a sec .")
            speak(get_jokes())
            print(f'''
                ====In case you didn't understood my accent :)====

                {get_jokes()}
            ''')
            suggestion = input(f"Did you like it, Yes(Y) or No(N) ? => ").lower()
            print(suggestion)
            if suggestion == "y":
                speak("Thanks, sir !!")
            else:
                speak("I'll try for a good one next time sir .")
            

        elif 'an advice' in query:
            speak("Okay sir, I have something to suggest. May I ?")
            speak(f"Very well sir, Here we go then. {get_random_advice()}")
            print(f"I have printed it as well in case you were unable to understand my accent of speech.\n{get_random_advice}")








            
            