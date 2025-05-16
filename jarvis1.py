import speech_recognition as sr
import pyttsx3
import webbrowser
import time
import os
import random
import sys
import shutil
import psutil  # Used to manage system processes
from datetime import datetime  

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 200)  
engine.setProperty("volume", 1.0)  

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to user commands using the microphone."""
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300  
    recognizer.pause_threshold = 1  
    
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  
        
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio, language="en-IN")  
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
            return ""
        except sr.RequestError:
            print("Check your internet connection or microphone.")
            return ""
        except sr.WaitTimeoutError:
            print("No input detected. Please speak again.")
            return ""

def jarvis_intro():
    """Introduce Jarvis to the user."""
    intro_text ="""Hello, I am Jarvis, your personal AI assistant. 
    I can assist you with various tasks like opening applications, 
    searching the web, telling the time and date, playing music, and much more. 
    Just say a command, and I'll handle it for you.
    """
    print(intro_text)
    speak(intro_text)

def get_time():
    """Speak the current time."""
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")  
    speak(f"The time is {current_time}")

def get_date():
    """Speak the current date."""
    today = datetime.now()
    current_date = today.strftime("%A, %d %B %Y")  
    speak(f"Today's date is {current_date}")

def open_application(app_name):
    """Open an application or system utility based on user input."""
    app_paths = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "chrome": "chrome",
        "vlc": "vlc",
        "task manager": "taskmgr.exe",
        "file manager": "explorer.exe",
        "control panel": "control.exe",
        "settings": "start ms-settings:",
    }
    
    if app_name in app_paths:
        app_path = shutil.which(app_paths[app_name])
        if app_path:
            os.startfile(app_path)
            speak(f"Opening {app_name}")
        else:
            speak(f"{app_name} is not installed on your system.")
    elif "drive" in app_name:
        drive_letter = app_name.split()[0].upper()
        os.system(f"explorer {drive_letter}:\\")
        speak(f"Opening {drive_letter} drive")
    else:
        speak(f"Sorry, I don't know how to open {app_name}.")

def play_music():
    """Play a random song from the user's music folder."""
    music_folder = os.path.expanduser("~/Music")
    try:
        songs = [song for song in os.listdir(music_folder) if song.endswith((".mp3", ".wav", ".flac"))]
        if songs:
            song = random.choice(songs)
            os.startfile(os.path.join(music_folder, song))
            speak(f"Playing {song}")
        else:
            speak("No music files found in the music folder.")
    except FileNotFoundError:
        speak("Music folder not found. Please check the path.")

def stop_music():
    """Stop any running music players."""
    music_players = ["vlc.exe", "wmplayer.exe", "groove.exe", "itunes.exe","Media player.exe"]  # Add more if needed
    found = False

    for process in psutil.process_iter(attrs=["pid", "name"]):
        try:
            process_name = process.info["name"].lower()
            if process_name in music_players:
                os.kill(process.info["pid"], 9)  # Forcefully terminate the process
                found = True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    if found:
        speak("Music stopped.")
    else:
        speak("No music is playing at the moment.")

def perform_task(command):
    """Perform tasks based on voice commands."""
    if "search" in command:
        query = command.replace("search", "").strip()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Searching for {query}")
    if "search youtube for" in command:
        query = command.replace("search youtube for", "").strip()
        if query:
            url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(url)
            speak(f"Searching YouTube for {query}")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "open" in command or "launch" in command:
        app_name = command.replace("open", "").replace("launch", "").strip()
        open_application(app_name)
    elif "play" in command and "on youtube" in command:
        query = command.replace("play", "").replace("on youtube", "").strip()
        if query:
            url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(url)
            speak(f"Playing {query} on YouTube")
    
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    
    elif "time" in command:
        get_time()

    elif "date" in command:
        get_date()

    elif "play music" in command or "start music" in command:
        play_music()

    elif "stop music" in command:
        stop_music()

    elif "stop" in command or "exit" in command:
        speak("Goodbye  Have a great day!")
        sys.exit()

    else:
        speak("I'm not sure how to respond to that.")

def main():
    """Main function to run the AI assistant."""
    jarvis_intro()
    speak("How can I assist you today?")
    
    while True:
        command = listen()
        if command:
            perform_task(command)

if __name__ == "__main__":
    main()
    