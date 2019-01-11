from microbit import *
import radio

radio.on()
radio.reset()

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        buttonNum = 5
        sleep(100)
    elif button_a.is_pressed():
        buttonNum = 10
    elif button_b.is_pressed():
        buttonNum = 11
    else:
        buttonNum = 0
    radio.send(str(buttonNum))