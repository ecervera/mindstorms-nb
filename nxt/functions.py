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
            print("No es pot connectar, ja hi ha un altre programa. Has de desconnectar-lo abans!")
        elif errno==13:
            print("No es pot connectar, el dispositiu no està emparellat.")
        elif errno == 112:
            print("No es troba el brick, assegurat que estiga encés.")
        else:
            print("Error %d: %s" % (errno, errmsg))

def disconnect(brick):
    brick.sock.close()

def forward():
    mB.run(-100)
    mC.run(100)
    
def backward():
    mB.run(100)
    mC.run(-100)
    
def stop():
    mB.brake()
    mC.brake()
