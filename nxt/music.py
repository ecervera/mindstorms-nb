from functions import play_tone
import math
import time

def freq(fbase,octava):
    if octava == 0:
        return int(fbase)
    else:
        return int(fbase*math.pow(2,octava))
        
def Silenci(t=1):
    time.sleep(t)
    
def Do(t=1, octava=0):
    f = freq(261.63,octava)
    play_tone(f,t)

def Re(t=1, octava=0):
    f = freq(293.66,octava)
    play_tone(f,t)

def Mi(t=1, octava=0):
    f = freq(329.63,octava)
    play_tone(f,t)

def Fa(t=1, octava=0):
    f = freq(349.23,octava)
    play_tone(f,t)
        
def Sol(t=1, octava=0):
    f = freq(392.00,octava)
    play_tone(f,t)
        
def La(t=1, octava=0):
    f = freq(440.00,octava)
    play_tone(f,t)

def Si_bemol(t=1, octava=0):
    f = freq(466.16,octava)
    play_tone(f,t)

def Si(t=1, octava=0):
    f = freq(493.88,octava)
    play_tone(f,t)
    