from microbit import *
import radio

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
while True:
    value = radio.receive()
    if value != None:
        value = int(value)
        if value == 10:
            left()
        elif value == 11:
            right()
        elif value == 12:
            back()
        elif value == 13:
            forward()
        elif value == 5:
            stop()
        elif value == 1:
            pin0.write_analog(180)
        elif value == 3:
            pin0.write_analog(1)
        else:
            pin0.write_analog(0)
