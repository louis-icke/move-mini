'''Forwards:  A
   Backwards: B
   Stop:      Both'''
from microbit import *
import radio

radio.on()
radio.reset()

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        buttonNum = 5
        sleep(100)
    elif button_a.is_pressed():
        buttonNum = 12
    elif button_b.is_pressed():
        buttonNum = 13
    else:
        buttonNum = 0
    radio.send(str(buttonNum))
