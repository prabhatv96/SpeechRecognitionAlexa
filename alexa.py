import speech_recognition as sr
import pyttsx3,pywhatkit
import datetime
import wikipedia

r = sr.Recognizer()
engine = pyttsx3.init()

#voice change
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

#speaking
engine.say("Hello, I am your alexa")
engine.say("What can I do for you?")
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            command = r.recognize_google(audio)
            print(command)
            # talk(command)
    except sr.UnknownValueError:
        print("Didn't get that. Try Again")
    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play','')
        talk('playing')
        print('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("Current time is "+time)

    elif 'who' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info )

    elif 'search' in command:
        command = command.replace('search','')
        pywhatkit.search(command)

    else:
        talk("Please say it again")

while True:
    run_alexa()
