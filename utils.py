import pyttsx3
import speech_recognition as sr
from datetime import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    now = datetime.now()
    hour = now.strftime("%H")
    min = now.strftime("%M")

    print(hour, ":", min)

    if hour >= '00' and hour < '12':
        speak("good morning, have a nice day")

    elif hour >= '12' and hour < '18':
        speak("good afternoon")

    else:
        speak("good Evening")

    speak("I am your Assistant.How may I help you shubham?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        query = None

    return query
