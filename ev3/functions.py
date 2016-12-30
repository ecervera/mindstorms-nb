import json
import shutil

def configure(n):
    config = {
        'version' : 'ev3',
        'number' : n
    }
    with open('../task/robot_config.json', 'w') as f:
        json.dump(config, f)
    shutil.copyfile('./functions.py', '../task/functions.py')
    print("\x1b[32mConfiguració completa, podeu continuar.\x1b[0m")

import rpyc
    
def connect():
    global conn
    global ev3
    global mB; global mC
    global ts; global gy; global us; global cl; global so
    global snd
    global tempo
    global connected_robot
    with open('robot_config.json', 'r') as f:
         config = json.load(f)
    n = config['number']
    try:
        address = {1: '192.168.1.27'}
        conn = rpyc.classic.connect(address[n]) 
        ev3 = conn.modules['ev3dev.ev3']
        mB = ev3.LargeMotor('outB')
        mC = ev3.LargeMotor('outC')
        ts = ev3.TouchSensor()
        #gy = ev3.GyroSensor()
        #gy.mode='GYRO-ANG'
        #so = ev3.Sensor('in2')
        so = ev3.SoundSensor('in2')
        so.mode='DB'
        us = ev3.UltrasonicSensor()
        us.mode='US-DIST-CM'
        cl = ev3.ColorSensor()
        cl.mode='COL-REFLECT'
        snd = ev3.Sound()
        tempo = 0.25
        connected_robot = n
        print("\x1b[32mRobot %d connectat.\x1b[0m" % n)
    except KeyError:
        print("\x1b[31mNúmero de robot incorrecte.\x1b[0m")
    except ConnectionRefusedError:
        print("\x1b[31mNo es pot connectar amb el robot.\x1b[0m")

def disconnect():
    try:
        conn.close()
        print("\x1b[32mRobot %d desconnectat.\x1b[0m" % connected_robot)
    except NameError:
        print("\x1b[31mNo hi ha connexió amb el robot.\x1b[0m")

def stop():
    try:
        mB.stop(stop_action="brake")
        mC.stop(stop_action="brake")
    except (NameError,EOFError):
        print("\x1b[31mNo hi ha connexió amb el robot.\x1b[0m")

def forward(speed=100):
    move(speed_B=abs(speed),speed_C=abs(speed))
    
def backward(speed=100):
    move(speed_B=-abs(speed),speed_C=-abs(speed))
    
def left(speed=100):
    move(speed_B=0,speed_C=abs(speed))

def right(speed=100):
    move(speed_B=abs(speed),speed_C=0)
    
def move(speed_B=0,speed_C=0):
    max_speed = 200
    speed_B = int(speed_B)
    speed_C = int(speed_C)
    if speed_B > 100:
        speed_B = 100
        print("\x1b[33mLa velocitat màxima és 100.\x1b[0m")
    if speed_C > 100:
        speed_C = 100
        print("\x1b[33mLa velocitat màxima és 100.\x1b[0m")
    try:
        mB.run_forever(speed_sp=int(speed_B*max_speed/100))
        mC.run_forever(speed_sp=int(speed_C*max_speed/100))
    except (NameError,EOFError):
        print("\x1b[31mNo hi ha connexió amb el robot.\x1b[0m")
    
def touch():
    return bool(ts.value())

#def gyro():
#    return gy.value()

def sound():
    return so.value()/10

def ultrasonic():
    return us.value()/10

def light():
    return cl.value()

def beep():
    snd.beep()
    
def play_tone(f,t):
    snd.tone(f,int(t*1000*tempo)).wait()
    
def speak(s):
    snd.speak(s).wait()