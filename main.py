import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import google.generativeai as genai


genai.configure(api_key="Your_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")


# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open spotify" in c.lower():
        webbrowser.open("https://spotify.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    else:
        # let ai handle the request
        response = model.generate_content(
            "You are Jarvis a virtual assistant. Please provide informative and concise answers without using asterisks or hashtags. your content should be such that it can be used dor text to speech"
            + c
        )
        speak(response.text)


if __name__ == "__main__":
    speak(" Initializing Jarvis...... ")
    while True:
        r = sr.Recognizer()

        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Ya")

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
