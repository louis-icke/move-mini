from microbit import *
import radio
channel = 1

def left():
    pin1.write_analog(1)
    pin2.write_analog(1)

def right():
    pin1.write_analog(180)
    pin2.write_analog(180)

def forward():
    pin1.write_analog(1)
    pin2.write_analog(180)

def back():
    pin1.write_analog(180)
    pin2.write_analog(1)

def stop():
    pin1.write_analog(0)
    pin2.write_analog(0)
    

pin0.set_analog_period(20)
pin1.set_analog_period(20)
pin2.set_analog_period(20)
radio.on()
radio.config(channel=channel)
while True:
    value = radio.receive()
    if value != None:
        joy = int(value[1])
        but = int(value[0])
        if joy == 1:
            left()
        elif joy == 2:
            right()
        elif joy == 3:
            back()
        elif joy == 4:
            forward()
        else:
            stop()
            
        if but == 1:
            pin0.write_analog(180)
        elif but == 3:
            pin0.write_analog(1)
        else:
            pin0.write_analog(0)
