import nxt.bluesock
import nxt.motor

import math
import time

from bluetooth.btcommon import BluetoothError

def connect(n):
    global brick
    global mB; global mC
    global s1; global s2; global s3; global s4
    global tempo
    global connected_robot
    try:
        address = {5: '00:16:53:08:D5:59', 12: '00:16:53:1A:C6:BD'}
        brick = nxt.bluesock.BlueSock(address[n]).connect()
        mB = nxt.motor.Motor(brick, nxt.motor.PORT_B)
        mC = nxt.motor.Motor(brick, nxt.motor.PORT_C)
        s1 = nxt.sensor.Touch(brick, nxt.sensor.PORT_1)
        s2 = nxt.sensor.Sound(brick, nxt.sensor.PORT_2)
        s3 = nxt.sensor.Light(brick, nxt.sensor.PORT_3)
        s3.set_illuminated(True)
        s4 = nxt.sensor.Ultrasonic(brick, nxt.sensor.PORT_4)
        tempo = 0.5
        connected_robot = n
        print("\x1b[32mRobot %d connectat.\x1b[0m" % n)
    except BluetoothError as e:
        errno, errmsg = eval(e.args[0])
        if errno==16:
            print("\x1b[31mNo es pot connectar, hi ha un altre programa ocupant la connexió.\x1b[0m")
        elif errno==13:
            print("\x1b[31mNo es pot connectar, el dispositiu no està emparellat.\x1b[0m")
        elif errno == 112:
            print("\x1b[31mNo es troba el brick, assegurat que estiga encés.\x1b[0m")
        else:
            print("Error %d: %s" % (errno, errmsg))
    except KeyError:
        print("\x1b[31mNúmero de robot incorrecte.\x1b[0m")

def disconnect():
    try:
        brick.sock.close()
        print("\x1b[32mRobot %d desconnectat.\x1b[0m" % connected_robot)
    except NameError:
        print("\x1b[31mNo hi ha connexió amb el robot.\x1b[0m")

def stop():
    try:
        mB.brake()
        mC.brake()
    except NameError:
        print("\x1b[31mNo hi ha connexió amb el robot.\x1b[0m")

def forward(speed=100,speed_B=100,speed_C=100):
    move(speed_B=min(abs(speed),abs(speed_B)),speed_C=min(abs(speed),abs(speed_C)))
    
def backward(speed=100,speed_B=100,speed_C=100):
    move(speed_B=-min(abs(speed),abs(speed_B)),speed_C=-min(abs(speed),abs(speed_C)))
    
def left(speed=100):
    move(speed_B=0,speed_C=abs(speed))

def right(speed=100):
    move(speed_B=abs(speed),speed_C=0)

def move(speed_B=0,speed_C=0):
    max_speed = 100
    speed_B = int(speed_B)
    speed_C = int(speed_C)
    if speed_B > 100:
        speed_B = 100
        print("\x1b[33mLa velocitat màxima és 100.\x1b[0m")
    if speed_B < -100:
        speed_B = -100
        print("\x1b[33mLa velocitat màxima és 100.\x1b[0m")
    if speed_C > 100:
        speed_C = 100
        print("\x1b[33mLa velocitat màxima és 100.\x1b[0m")
    if speed_C < -100:
        speed_C = -100
        print("\x1b[33mLa velocitat màxima és 100.\x1b[0m")
    try:
        mB.run(-int(speed_B*max_speed/100))
        mC.run(int(speed_C*max_speed/100))
    except NameError:
        print("\x1b[31mNo hi ha connexió amb el robot.\x1b[0m")

def touch():
    return s1.is_pressed()
    
def sound():
    return s2.get_loudness()

def light():
    return s3.get_lightness()

def ultrasonic():
    return s4.get_distance()

def play_sound(s):
    brick.play_sound_file(False, bytes((s+'.rso').encode('ascii')))

def say(s):
    play_sound(s)

def play_tone(f,t):
    try:
        brick.play_tone_and_wait(f, int(t*1000*tempo))
        time.sleep(0.01)
    except:
        pass

from IPython.display import clear_output

def read_and_print(sensor):
    try:
        while True:
            clear_output(wait=True)
            print(sensor())
    except KeyboardInterrupt:
        pass