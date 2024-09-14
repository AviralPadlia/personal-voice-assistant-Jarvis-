#talklis
def lis(mic,r):
    with mic as source:
            print("listening...")
            audio=r.listen(source)
            r.pause_threshold=1
            r.energy_threshold=4000
            command=r.recognize_google(audio)
            print(command)
            return command
        
def talk(engine,text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def takeCmd(mic,r,engine):
    try:
        command=lis(mic,r)
        return command
    except:
        talk(engine,"Sorry!...I didn't get it, Please speak again...")
        command=takeCmd(mic,r,engine)
        return command
