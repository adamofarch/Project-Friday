########</Developed by @realdarkstar>########

# GitHub Repo: https://github.com/realdarkstar/Project-Friday-on-Python
# Follow me on Instagram: https://instagram.com/realdarkstar
# For suggestions and bug reports: https://github.com/realdarkstar/Project-Friday-on-Python/issues

'''IMPORTANT(For DEVs): The Traceback and TypeError raised after the execution of this code is because
                        of the module pywhatkit i figured and they're harmless to the code ofcourse since, 
                        it's being generated from the source of pywhatkit module and being raised after execution
                        I have supressed Traceback using sys module but we can't remove the module itself to fix
                        both of the errors at once since it is required to execute some functions of this
                        code to make it a feature rich AI. So we have to ignore the TypeError unfortunately. 
                        I will update the code as soon as i'll be able to find a appropriate way to fix the
                        error or to supress it.  
'''

from email.message import EmailMessage
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
from paths import path
import smtplib
import time
import pyautogui as ptg
from exec_greet import exec_greet
import sys

USERNAME = config("USER")
BOTNAME = config("BOT")

EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")

NEWS_API_KEY = config("NEWS_API_KEY")

OPEN_WEATHER_APPID = config("OPEN_WEATHER_APPID")

TMDB_API_KEY = config("TMDB_API_KEY")

# This line of syntax is used to supress any TraceBack raised after execution of this code
sys.tracebacklimit=0

# Text to Speech engine used in this code, helps us to take text input from user and convert it to speech
engine = pyttsx3.init('sapi5')

# Setting the values like words per minute spoken by the FRIDAY and volume based on the pyttsx3 module using setProperty method 
engine.setProperty('rate', 195)
engine.setProperty('volume', 1.0)

# Fetching the voices provided by the module pyttsx3(has only 2 voices stored in the module by default) using getProperty method
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    '''Speak function will help our AI to be able to speak using pyttsx3 module'''
    engine.say(text)
    engine.runAndWait()

def greet_user():
    '''Greet function will be used to allow AI to greet the user'''
    hour = datetime.now().hour
    if (hour >= 0) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good AfterNoon {USERNAME}")
    elif (hour >= 16) and (hour < 21):
        speak(f"Good Evening {USERNAME}")
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
        query = r.recognize_google(audio, language='en-in')
        print(query)
        if not 'exit' in query or 'stop' in query:
            speak(choice(exec_greet))
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
        email = EmailMessage()
        email['To'] = receiver_address
        email['Subject'] = subject
        email['From'] = EMAIL
        email.set_content(message)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(email)
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

def get_weather(city):
    result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={OPEN_WEATHER_APPID}").json()
    weather = result["weather"][0]["main"]
    temperature = result["main"]["temp"]
    feels_like = result["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"

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

    while 1:
        query = take_user_input().lower()

        if 'open code' in query:
            os.startfile(path['vs code'])

        elif 'open calculator' in query:
            sp.Popen(path['calculator'])

        elif 'open notepad' in query:
            os.startfile(path['notepad'])
        
        elif 'open putty' in query:
            os.startfile(path['putty'])

        elif 'open brave' in query:
            os.startfile(path['brave'])

        elif 'open spotify' in query:
            os.startfile(path['spotify'])
        
        elif 'open command prompt' in query or 'open cmd' in query:
            os.Popen(path['cmd'])

        elif 'open youtube' in query:
            webbrowser.Chrome(path['chrome']).open_new_tab("youtube.com")

        elif 'open facebook' in query or 'open fb' in query:
            webbrowser.Chrome(path['chrome']).open_new_tab("facebook.com")

        elif 'open stackoverflow' in query or 'open stack overflow' in query:
            webbrowser.Chrome(path['chrome']).open_new_tab("stackoverflow.com")

        elif 'open github' in query:
            webbrowser.Chrome(path['chrome']).open_new_tab("github.com")

        elif 'open a website' in query:
            speak("Which website you want to open sir")
            site = take_user_input()
            if '.com' in site:
                if 'None' in site:
                    speak("Please tell me a valid input")
                else:
                    webbrowser.Chrome(path['chrome']).open_new_tab(f"{site}")
            else:
                if 'None' in site:
                    speak("Please tell me a valid input")
                else:
                    pywhatkit.search(site)
                

        elif 'my ip' in query:
            result = requests.get('https://api64.ipify.org?format=json').json()
            ip = result["ip"]
            print(f"Your IP address is => {ip}")
            speak(f"Your IP address is {ip}")

        elif 'time' in query:
            Time = datetime.now().strftime("%H:%M:%S")
            print(Time)
            speak(f"The time is {Time}")

        elif 'play music' in query:
            res = os.listdir(path['songs'])
            for item in res:
                print(res, sep="\n")
            speak("Which song would you like to play sir")
            os.startfile(os.path.join(path['songs'], res[int(input("Enter the index number of your song file => "))]))

        elif 'on wikipedia' in query:
            speak("searching wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            print(results)
            speak(results)

        elif 'on google' in query:
            speak("searching....")
            query = query.replace("search", "")
            query = query.replace("on google", "")
            pywhatkit.search(query)

        elif 'on youtube' in query or 'on yt' in query:
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
            time.sleep(10.0)
            ptg.press("enter")
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

        elif 'news headlines' in query or 'latest news' in query:
            speak("please wait.....")
            result = get_latest_news()
            for item in result:
                print(item, sep="\n")
            speak(result)

        elif 'weather today' in query:
            speak("Wait a second")
            result = requests.get('https://api64.ipify.org?format=json').json()
            ip = result["ip"]
            city = requests.get(f"https://ipapi.co/{ip}/city/").text
            weather, temperature, feels_like = get_weather(city)
            print(f"Weather: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
            speak(f"The weather will be {weather} in your city. The Temperature will be {temperature} and it feels_like {feels_like} in your city.")

        elif 'trending movies' in query:
            speak("Please Wait.....")
            speak("There you go, sir")
            movies = get_trending_movies()
            speak(f"Top Trending movies now are : ")
            for item in movies:
                print(item, sep="\n")
            speak(movies)

        elif 'tell me a joke' in query:
            speak("Wait a second")
            joke = get_jokes()
            speak(joke)
            print(f'''
                ====In case you didn't understood my accent :)====

                => {joke}
            ''')
            suggestion = input(f"Did you like it, Yes(Y) or No(N) ? => ").lower()
            print(suggestion)
            if suggestion == "y":
                speak("Thanks, sir !!")
            else:
                speak("I'll try for a good one next time sir .")
            

        elif 'advice' in query:
            speak("Okay sir, I have something to suggest. May I ?")
            advice = get_random_advice()
            speak(f"Very well sir, Here we go then. {advice}")
            print(f"=> {advice}")
