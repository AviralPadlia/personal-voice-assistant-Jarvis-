#jokes
import pyjokes
import talklis as tl

def joke(engine):
    tl.talk(engine,pyjokes.get_joke())