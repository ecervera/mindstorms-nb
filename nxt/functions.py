import nxt.bluesock
import nxt.motor

from bluetooth.btcommon import BluetoothError

def connect(n):
    global brick
    global mB
    global mC
    try:
        address = {5: '00:16:53:08:D5:59', 12: '00:16:53:1A:C6:BD'}
        brick = nxt.bluesock.BlueSock(address[n]).connect()
        mB = nxt.motor.Motor(brick, nxt.motor.PORT_B)
        mC = nxt.motor.Motor(brick, nxt.motor.PORT_C)
    except BluetoothError as e:
        errno, errmsg = eval(e.args[0])
        if errno==16:
            print("\x1b[31mNo es pot connectar, ja hi ha un altre programa. Has de desconnectar-lo abans!\x1b[0m")
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
    except NameError:
        print("\x1b[31mNo hi ha connexió amb el robot.\x1b[0m")
'''
def forward():
    mB.run(-100)
    mC.run(100)
    
def backward():
    mB.run(100)
    mC.run(-100)
'''
def stop():
    mB.brake()
    mC.brake()

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
    if speed_C > 100:
        speed_C = 100
        print("\x1b[33mLa velocitat màxima és 100.\x1b[0m")
    try:
        mB.run(-int(speed_B*max_speed/100))
        mC.run(int(speed_C*max_speed/100))
    except NameError:
        print("\x1b[31mNo hi ha connexió amb el robot.\x1b[0m")
  