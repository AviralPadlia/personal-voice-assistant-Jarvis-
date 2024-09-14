import tkinter
from tkinter import *
import tkinter.font as font
import main

def onStart():
    main.jarvis()

def onMute():
    if mute["text"]=="Mute":
        mute["text"]="Unmute"
    else:
        mute["text"]="Mute"
    #while True:
        
root=tkinter.Tk()
root.geometry("800x900+150+30")
root.title("JARVIS")

frame1= Frame(root,bg="#28282B")
frame1.pack(fill="both",expand=True)

frame2 = Frame(root,bg="#28282B")
frame2.pack(fill="both",expand=True)

myFont=font.Font(size=15)
l=Label(frame1,text="Conversation",bg="#28282B",font=("Roboto"),fg="Light Blue")
l.pack(side=TOP,padx=15,anchor=NW)
l['font']=myFont

t=Text(frame1,bg="#000000",fg="#ffffff",font = ("Verdana", 15),width=50,bd=3,relief=SUNKEN)
t.pack(side=LEFT,expand=True,padx=15)

start= Button(frame2,text="Start",border=3,bg="dark grey",font=("Verdana",15),relief=RAISED,command=onStart)
start.pack(side =LEFT,padx=30,pady=10,expand=True,fill="both")

mute= Button(frame2,text="Mute",border=3,bg="dark grey",font=("Verdana",15),relief=RAISED,command=onMute)
mute.pack(side =LEFT,padx=30,pady=10,expand=True,fill="both")

ext= Button(frame2,text = "Exit",border=3,bg="dark grey",font=("Verdana",15),relief=RAISED,command=root.destroy)
ext.pack(side =LEFT,padx=30,pady=10,expand=True,fill="both")

#main.jarvis()
root.mainloop()

