import pyttsx3
import speech_recognition as sr
import webbrowser
from datetime import datetime

engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def wish_me():
    """Wish the user based on the current time."""
    hour = datetime.now().hour

    if 0 <= hour < 12:
        speak("Good Morning Boss...")
    elif 12 <= hour < 17:
        speak("Good Afternoon Master...")
    else:
        speak("Good Evening Sir...")

def take_command():
    """Listen for a voice command and return it as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def process_command(command):
    """Process the given voice command."""
    command = command.lower()
    
    if 'hey' in command or 'hello' in command:
        speak("Hello Boss, I am Jarvis, How May I Help You?")
    elif "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google...")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening Youtube...")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook...")
    elif 'what is' in command or 'who is' in command or 'what are' in command:
        webbrowser.open(f"https://www.google.com/search?q={command.replace(' ', '+')}")
        speak(f"This is what I found on the internet regarding {command}")
    elif 'wikipedia' in command:
        webbrowser.open(f"https://en.wikipedia.org/wiki/{command.replace('wikipedia', '').strip()}")
        speak(f"This is what I found on Wikipedia regarding {command}")
    elif 'time' in command:
        time = datetime.now().strftime("%H:%M")
        speak(f"The current time is {time}")
    elif 'date' in command:
        date = datetime.now().strftime("%B %d")
        speak(f"Today's date is {date}")
    elif 'calculator' in command:
        webbrowser.open('Calculator:///')
        speak("Opening Calculator")
    elif "open gpt" in command:
        webbrowser.open("https://chatgpt.com/?oai-dm=1")
        speak("Opening ChatGPT...")
    elif "quit" in command:
        webbrowser.open("https://thumb.ac-illust.com/77/77583fec2040e0e12efae9a38d52f5b4_w.jpeg")
        speak("You may close the tab...")
    else:
        webbrowser.open(f"https://www.google.com/search?q={command.replace(' ', '+')}")
        speak(f"I found some information for {command} on Google")

