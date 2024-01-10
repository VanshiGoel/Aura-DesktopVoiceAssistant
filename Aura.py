import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import subprocess
import psutil 

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''This function wishes the user according to time'''

    hour=int(datetime.datetime.now().hour)
    if(hour<12):
        speak("GoodMorning Vanshika")
    elif(hour>=12 and hour<17):
        speak("GoodAfterNoon Vanshika")
    else:
        speak("GoodEvening Vanshika")

    speak("I am Aura. Please tell me how may I help you?")

def takeCommand():
    '''This Function takes microphone input and converts it into a string'''

    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    
    return query

def close_application(application_name):
    try:
        for process in psutil.process_iter(['pid', 'name']):
            if application_name.lower() in process.info['name'].lower():
                subprocess.run(["taskkill", "/f", "/pid", str(process.info['pid'])], check=True)
                print(f"{application_name} closed successfully.")
                return

        print(f"{application_name} is not running.")
    except subprocess.CalledProcessError:
        print(f"Failed to close {application_name}.")



if __name__=="__main__":
    wishMe()

    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia..")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        
        elif 'open gfg' in query:
            webbrowser.open("https://www.geeksforgeeks.org")
        
        elif 'open lc' in query:
            webbrowser.open("https://www.leetcode.com")
        
        elif 'open codechef' in query:
            webbrowser.open("https://www.codechef.com")
        
        elif 'open chat gpt' in query:
            webbrowser.open("https://chat.openai.com/")
        
        elif 'play music' in query:
            music_dir="D:\songs"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"Ma'am the time is {strtime}")
        
        elif 'open vs code' in query:
            codepath="C:\\Users\Vanshika\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif 'open word' in query:
            codepath="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codepath)
        
        elif "close application" in query:
            application_name = query.split("application")[-1].strip()
            close_application(application_name)
        
        elif 'quit' in query:
            speak("Thank you")
            exit(1)


