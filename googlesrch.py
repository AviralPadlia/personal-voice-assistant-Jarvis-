#googlesrch
import pywhatkit as kt
import wikipedia
import keyboard as kb
import time
import os
import talklis as tl

def googleSearch(mic,r,engine,command):
    command=command.replace("search","")
    tl.talk(engine,"Searching"+command)
    kt.search(command)
    try:
        txt=wikipedia.summary(command,sentences=1)
        tl.talk(engine,txt)
    except:
        pass
    while True:
        command=tl.takeCmd(mic,r,engine)
        #command.lower()

        if "refresh" in command or "reload" in command:         #done
            kb.press_and_release('F5')
        
        elif "search" in command or "what is" in command or "who is" in command or "how to" in command:
            command=command.replace("search","")
            kt.search(command)

        elif "full screen" in command or "maximize" in command:         #done
            kb.press_and_release('F11')
            
        elif "minimise" in command:
            kb.press_and_release('win+down arrow')
            
        elif "stop" in command:
            kb.press_and_release('esc')
            
        elif "move down" in command or "scroll down" in command:         #done
            kb.press_and_release('spacebar')
            
        elif "home page" in command:         #done
            kb.press_and_release('alt+home')
            
        elif "back" in command:         #done
            kb.press_and_release('alt+left arrow')
            
        elif "next" in command or "forward" in command:         #done
            kb.press_and_release('alt+right arrow')
            
        elif "increase font" in command:
            kb.press_and_release('ctrl+'+'plus')
            
        elif "decrease font" in command:                    #tochk
            kb.press_and_release('ctrl+'+'minus')

        elif "reset font" in command:
            kb.press_and_release('ctrl+0')

        elif "select all" in command:
            kb.press_and_release('ctrl+a')

        elif "copy" in command:
            kb.press_and_release('ctrl+c')
            tl.talk(engine,"text copied successfully")

        elif "add bookmark" in command or "add book mark" in command:
            kb.press_and_release('ctrl+d')

        elif "new window" in command:         #done
            kb.press_and_release('ctrl+n')
            command=tl.takeCmd(mic,r,engine)
            if "search" in command:
                kb.write(command.replace("search",""))
                kb.press_and_release('enter')

        elif "new tab" in command:         #done
            kb.press_and_release('ctrl+t')
            if "search" in command:
                kb.write(command.replace("search",""))
                kb.press_and_release('enter')
                
        elif "Close tab" in command:         #done
            kb.press_and_release('ctrl+w')

        elif "switch tab" in command:           #tochk
            tab=command.replace("switch tab to","")
            toTab=f'ctrl+{tab}'
            kb.press_and_release(toTab)

        elif "next tab" in command or "switch tab" in command:
            kb.press_and_release('ctrl+tab')

        elif "incognito tab" in command or "private tab" in command:
            kb.press_and_release('ctrl+shift+n')

        elif "reopen tab" in command or "re open tab" in command:
            kb.press_and_release('ctrl+shift+t')

        elif "completely close" in command or "close window" in command:         #done
            kb.press_and_release('ctrl+shift+w')
            break

        elif "notepad" in command:
            os.startfile("Notepad")
            time.sleep(2)
            kb.press_and_release('ctrl+v')

        elif "close" in command:         #done
            break

#copy to notepad
#search