import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    """Speak the given text using text-to-speech."""
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    """Listen for a voice command and return it as text."""
    with sr.Microphone() as source:
        print("Listening... (say a command)")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.WaitTimeoutError:
            print("No speech detected. Please try again.")
            speak("No speech detected. Please try again.")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Could not request results from the speech recognition service.")
            speak("Could not request results from the speech recognition service.")
        except OSError:
            print("Microphone not found or not working.")
            speak("Microphone not found or not working.")
        return None

def handle_command(command):
    """Handle the recognized command."""
    if command is None:
        return False
    if "hello" in command:
        speak("Hello! How can I help you today?")
    elif "what time is it" in command:
        now = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")
    elif "open google" in command:
        speak("Opening Google in your browser.")
        webbrowser.open("https://www.google.com")
    elif "exit" in command:
        speak("Goodbye!")
        return True
    else:
        speak("Sorry, I can only respond to hello, what time is it, open google, or exit.")
    return False

def main():
    print("--- Python Voice Assistant ---")
    speak("Voice Assistant started. Say a command.")
    while True:
        command = listen()
        if handle_command(command):
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        speak("Goodbye!")
    except OSError:
        print("Microphone not found or not working.")
        speak("Microphone not found or not working.")
