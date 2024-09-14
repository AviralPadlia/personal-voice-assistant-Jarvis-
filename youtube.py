import pywhatkit as kt
import keyboard as kb

import talklis as tl

def youtube(mic,r,engine,command):
    command=command.replace("play","")
    tl.talk(engine,"Playing"+command)
    kt.playonyt(command)
    while True:
        command=tl.takeCmd(mic,r,engine)

        if "search" in command:
            kb.press_and_release("/")
            tl.talk(engine,"what do you want to play sir")
            command=tl.takeCmd(mic,r,engine)
            kb.write(command)
            kb.press_and_release('enter')
        
        elif "pause" in command:
            kb.press_and_release('spacebar')
            
        elif "resume" in command:
            kb.press_and_release('spacebar')

        elif "mute" in command:     #tochk
            kb.press_and_release('m')

        elif "unmute" in command:
            kb.press_and_release('m')

        elif "forward" in command:
            kb.press_and_release('l')

        elif "backward" in command:
            kb.press_and_release('j')

        elif "Close tab" in command or "close video" in command or "completely close" in command or "close window" in command:         #done
            kb.press_and_release('ctrl+w')
            break