import speedtest
import talklis as tl

def checkspeed(engine):
    tl.talk(engine,"Checking your internet speed")
    speed=speedtest.Speedtest()
   
    download_speed="{:.2f}".format(speed.download()/1024/1024)
    uploading_speed="{:.2f}".format(speed.upload()/1024/1024)
    download_speed=str(download_speed)
    uploading_speed=str(uploading_speed)

    tl.talk(engine,"your downloading speed is "+download_speed+" Mb per second")
    tl.talk(engine,"your uploading sppeed  is"+uploading_speed+" Mb per second")
