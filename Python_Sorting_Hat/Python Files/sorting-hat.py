from time import sleep
from random import randint
from os import system
from gpiozero import Button

btn = Button(17)

def randomHouse():
    number = randint(1,4)

    if number == 1:
        system('mpg123 gryffindor.mp3')
        sleep(1)
    elif number == 2:
        system('mpg123 hufflepuff.mp3')
        sleep(1)
    elif number == 3:
        system('mpg123 ravenclaw.mp3')
        sleep(1)
    elif number == 4:
        system('mpg123 slytherin.mp3')
        sleep(1)

while True:
    if btn.is_pressed:
        randomHouse()