import rpyc

def connect(n):
    global conn
    global ev3
    global mB; global mC
    global ts; global gy; global us; global cl
    try:
        address = {1: '192.168.1.27'}
        conn = rpyc.classic.connect(address[n]) 
        ev3 = conn.modules['ev3dev.ev3']
        mB = ev3.LargeMotor('outB')
        mC = ev3.LargeMotor('outC')
        ts = ev3.TouchSensor()
        gy = ev3.GyroSensor()
        gy.mode='GYRO-ANG'
        us = ev3.UltrasonicSensor()
        us.mode='US-DIST-CM'
        cl = ev3.ColorSensor()
        cl.mode='COL-REFLECT'
        print("\x1b[32mRobot %d connectat.\x1b[0m" % n)
    except KeyError:
        print("\x1b[31mNúmero de robot incorrecte.\x1b[0m")
    except ConnectionRefusedError:
        print("\x1b[31mNo es pot connectar amb el robot.\x1b[0m")

def stop():
    try:
        mB.stop(stop_action="brake")
        mC.stop(stop_action="brake")
    except NameError:
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
    except NameError:
        print("\x1b[31mNo hi ha connexió amb el robot.\x1b[0m")
    
def touch():
    return ts.value()

def gyro():
    return gy.value()

def ultrasonic():
    return us.value()/10

def light():
    return cl.value()
