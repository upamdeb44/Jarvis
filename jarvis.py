import sys
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")
    speak(f"{speak}sir. ready to get started?")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 2
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        print("say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query= takeCommand().lower()

        #logic for exec tasks based on query
        if'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open zen' in query:
            zenPath = "C:\\Program Files\\Zen Browser\\zen.exe"
            os.startfile(zenPath)

        elif 'open firefox' in query:
            firefoxPath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(firefoxPath)

        elif 'play music' in query:
            music_dir = "C:\\Users\\KIIT0001\\Music\\MUSIC"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        
        elif 'open code' in query:
            codePath = "C:\\Users\\KIIT0001\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'shut up jarvis' in query:
            speak("Shutting down, sir.")
            sys.exit()