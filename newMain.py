import os
from turtledemo.penrose import start
import eel
from engine.command import *
from engine.features import *

def startProgram():

    eel.init("web")

    playAssistantSound()
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    eel.start("index.html",mode=None,host='localhost',block=True)

startProgram()