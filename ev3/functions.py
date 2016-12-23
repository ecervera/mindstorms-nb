import rpyc

def connect(ip):
    global conn
    global ev3
    global mB
    global mC
    conn = rpyc.classic.connect(ip) 
    ev3 = conn.modules['ev3dev.ev3']
    mB = ev3.LargeMotor('outB')
    mC = ev3.LargeMotor('outC')

def forward():
    mB.run_forever(speed_sp=200)
    mC.run_forever(speed_sp=200)
    
def backward():
    mB.run_forever(speed_sp=-200)
    mC.run_forever(speed_sp=-200)
    
def stop():
    mB.stop(stop_action="brake")
    mC.stop(stop_action="brake")