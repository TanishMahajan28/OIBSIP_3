import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import pyautogui

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I did not understand. Please try again.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def process_command(command):
    if "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        speak(time)
        
    elif "search" in command:
        search_query = command.replace("search", "").strip()
        search_url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(search_url)
        speak(f"Searching for {search_query}.")
    elif "take a screenshot" in command:
            pyautogui.screenshot("screenshot.png")
            speak("I took a screenshot for you.")
    elif "hello" in command:
        speak("Hello, Tanish. I hope you're having a nice day today!")
    elif "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    speak("Hello! How can I assist you today?")

    while True:
        command = listen()
        if command:
            process_command(command)