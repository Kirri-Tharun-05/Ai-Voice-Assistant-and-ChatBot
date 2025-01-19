import re
import struct
import time
import eel
import pvporcupine
import pyaudio
from playsound import playsound
import os
import subprocess
import pyautogui
from pyautogui import keyUp
from engine.command import speak
from engine.config import Assistant_name
import pywhatkit as kit
import webbrowser
from database import cursor
from engine.helper import extract_yt_term
from hugchat import hugchat
from urllib.parse import quote
@eel.expose
def playAssistantSound():
    music_dir="E:\\5th_sem_project\\pythonProject\\start_sound.mp3"
    playsound(music_dir)

def openFunctiion(query):
     query=query.replace(Assistant_name,"")
     query=query.replace("open","")
     query.lower()
     print(query)

     app_name=query.strip()
     if app_name!="":
         try:
             cursor.execute('SELECT path FROM sys_command WHERE name IN(?)',(app_name,))
             result=cursor.fetchall()
             print("Result : ",result)
             print("Length : ",len(result))
             if len(result)!=0:
                 print('1')
                 speak("Opening "+query)
                 print(result[0][0])
                 os.startfile(result[0][0])
             elif len(result)== 0 :
                 print('2')
                 cursor.execute(
                     'SELECT path FROM web_command where name IN (?)',(app_name,))
                 result=cursor.fetchall()

                 if len(result)!=0:
                     speak("Opening "+query)
                     webbrowser.open(result[0][0])
                 else:
                     speak("Opening "+query)
                     try:
                         os.system('start '+query)
                     except:
                         speak('not found')
         except Exception as e:
             speak("some thing went wrong")
             print(e)



def playYoutube(query):
    search_term = extract_yt_term(query)
    speak('Playing '+search_term+' on youtube')
    kit.playonyt(search_term)


def hot_word():
    porcupine=None
    paud=None
    audio_stream=None
    try:
        #pre trained keywords
        porcupine=pvporcupine.create(keywords=["alexa","jarvis"])
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)

        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            keyword_index=porcupine.process(keyword)

            if keyword_index>=0:
                print("Hotword Detected ")

                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    print(response)
    speak(response)
    return response



# Finding contacts in contact database0
def findContact(query):
    words_to_remove=['make','a','to','phone','call','send','message','whatapp','video']
    from engine.helper import remove_words
    query=remove_words(query,words_to_remove)
    print(query+" in featurs find contacts")

    try:
        print("inside try block")
        query=query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contact WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?",('%'+query+'%',query+'%'))
        result=cursor.fetchall()
        print(result[0][0] + "hello features")
        mobile_no_str=str(result[0][0])
        if not mobile_no_str.startswith('+91'):
            mobile_no_str='+91'+mobile_no_str
        
        return mobile_no_str, query
    except:
        speak('not exist in contacts')
        return 0, 0

# whatsapp automation features

def whatsapp(mobile_no,message,flag,name):
    if flag=='message':
        target_tab=12
        alexa_message="message sent successfully to "+name
    elif flag=='call':
        target_tab=7
        message=''
        alexa_message="calling "+name
    else:
        target_tab=6
        message=''
        alexa_message="starting video call with "+name

    # conveting a normal string to a url string
    encoded_message=quote(message)

    whatsapp_url=f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    full_command =f'start "" "{whatsapp_url}"'

    subprocess.run(full_command,shell=True)
    time.sleep(5)
    subprocess.run(full_command,shell=True)

    pyautogui.hotkey('ctrl','f')

    for i in range(1,target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(alexa_message)

