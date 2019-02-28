'''3rd Servo Up:   A
   3rd Servo Down: B
   Stop:           Both'''
from microbit import *
import radio

radio.on()
radio.config(channel=1)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        buttonNum = 5
        sleep(100)
    elif button_a.is_pressed():
        buttonNum = 1
    elif button_b.is_pressed():
        buttonNum = 3
    else:
        buttonNum = 0
    radio.send(str(buttonNum))
