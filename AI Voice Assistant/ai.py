import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# print(voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour >=12 and hour <=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak(" I am AI voice assisstant How may I help you ")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again")
        return "None"
    return query
    


if __name__ == '__main__':
    # wish_me()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            break
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            break
        elif 'open google' in query:
            webbrowser.open("google.com")
            break
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
            break
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)
            break
        
    
    