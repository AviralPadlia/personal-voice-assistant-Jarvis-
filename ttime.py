#ttime
import datetime
import talklis as tl

def start(mic,r,engine):
    try:
        command=tl.lis(mic,r)
        if "Jarvis" in command:
            hour = int(datetime.datetime.now().hour)
            if hour>=6 and hour<12:
                tl.talk(engine,"Good Morning Sir, How may I help you")

            elif hour>=12 and hour<18:
                tl.talk(engine,"Good Afternoon Sir, How may I help you")   

            else:
                tl.talk(engine,"Good Evening Sir, How may I help you")
                
            return
        tl.talk(engine,"Sorry!...I didn't understand, Please speak again...")
        start(mic,r,engine)
    except:
        tl.talk(engine,"Something went wrong...Please try again...")
        start(mic,r,engine)

def telltime(engine):
    x=datetime.datetime.now()
    tl.talk(engine,x.strftime("its %I:%M %p sir"))