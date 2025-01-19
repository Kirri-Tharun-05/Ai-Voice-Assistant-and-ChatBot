import pyttsx3
import speech_recognition as sr
import eel
import time
from eel import expose

def speak(text):
    text=str(text)
    engine=pyttsx3.init()
    engine.setProperty("rate",174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()


def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        eel.DisplayMessage('listening....')
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source,10,10)
    try:
        eel.DisplayMessage('recognizing....')
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(1)
    except Exception as e:
        return ""

    return query.lower()

@eel.expose()
def take_allCommands(message=1):

    if message==1:
        query=take_command()
        eel.senderText(query)
    else:
        query=message
        eel.senderText(query)
    try:
        print(query)

        if "open" in query:
            from engine.features import openFunctiion
            openFunctiion(query)

        elif "on youtube" in query:
                from engine.features import playYoutube
                playYoutube(query)

        elif "send a message" in query or"call" in query or "video call" in query:

            from engine.features import findContact, whatsapp
            message=""
            contact_no, name=findContact(query)
            if(contact_no != 0):
                if "send a message" in query:
                    message='message'
                    speak('what message to send')
                    query=take_command()
                elif "video call" in query:
                    message='video call'
                else:
                    message='call'
                whatsapp(contact_no,query,message,name)
                
        else:
            from engine.features import chatBot
            chatBot(query)
    except Exception as e:
        print(e)
    eel.home()
