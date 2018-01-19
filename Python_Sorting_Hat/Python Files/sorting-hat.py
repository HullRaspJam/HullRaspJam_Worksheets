import time
import random
import os
from gpiozero import Button

btn = Button(27)

def randomHouse():
    number = random.randint(1, 4)
    if number == 1:
        os.system('mpg123 gryffindor.mp3')
        time.sleep(1)
    elif number == 2:
        os.system('mpg123 hufflepuff.mp3')
        time.sleep(1)
    elif number == 3:
        os.system('mpg123 ravenclaw.mp3')
        time.sleep(1)
    elif number == 4:
        os.system('mpg123 slytherin.mp3')
        time.sleep(1)

while True:
    if btn.is_pressed():
        randomHouse()
