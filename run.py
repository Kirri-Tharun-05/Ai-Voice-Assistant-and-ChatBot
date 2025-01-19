import multiprocessing
import subprocess

def startAlexa():
    print("Process 1 is Running !")
    from newMain import startProgram
    startProgram()

def listenHotWord():
    print("Process 2 is Running !")
    from engine.features import hot_word
    hot_word()

if __name__ =='__main__':
    p1=multiprocessing.Process(target=startAlexa)
    p2=multiprocessing.Process(target=listenHotWord)
    p1.start()
    p2.start()
    p1.join()

    if p2.is_alive():
        p2.terminate()
        p2.join()

    print("system stop")