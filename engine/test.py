import pvporcupine
import pyaudio
import time
import struct
def hotword():
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


hotword()