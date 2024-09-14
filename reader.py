#reader
import PyPDF2
import talklis as tl

def notepad(mic,r,engine):
    file = open("text.txt","a")
    tl.talk(engine,"Say what would you like to write in the file")
    while True:
        command=tl.takeCmd(mic,r,engine)
        if "close" in command:
            file.close()
            tl.talk(engine,"File closed successfully")
            break
        else:  
            file.write(command)
            tl.talk(engine,"Would you want to add more or should I close it")

def readFile(engine):
    file=open("text.txt","r")
    data = file.read()
    tl.talk(engine,data)
    file.close()

def readPDF(engine):
    pdfFileObj = open('avi.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print(pdfReader.numPages)
    pageObj = pdfReader.getPage(0)
    #print(pageObj.extractText())
    tl.talk(engine,pageObj.extractText())
    pdfFileObj.close()