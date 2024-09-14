#main
import speech_recognition as sr
import pyttsx3

import ttime
import talklis as tl
import googlesrch as gs
import jokes
import reader
import youtube as yt
import internetspeed
import chatbot as cb

def jarvis(mic,r,engine):
    global command
    command=""
    while True:
        command=tl.takeCmd(mic,r,engine)
        command.lower()

        if "time" in command:
            ttime.telltime(engine)

        elif "search" in command:
            gs.googleSearch(mic,r,engine,command)

        elif "play" in command:
            yt.youtube(mic,r,engine,command)

        elif "joke" in command:
            jokes.joke(engine)

        elif "notepad" in command:
            reader.notepad(mic,r,engine)

        elif "read file" in command:
            reader.readFile(engine)

        elif "read PDF" in command:
            reader.readPDF(engine)

        elif "internet speed" in command:
            internetspeed.checkspeed(engine)

        else :
            response=cb.get_response(command)
            tl.talk(engine,response)
            if "bye" in command or "goodbye" in command or "tata" in command:
                exit()


engine = pyttsx3.init()
r=sr.Recognizer()
mic=sr.Microphone(device_index=1)
engine.setProperty('rate',170)

ttime.start(mic,r,engine)
jarvis(mic,r,engine)
     
