from turtle import *
from random import random
from datetime import datetime

SCREEN_SIZE = 600
NUM_CELLS = 50

SEEDED = False
x_seed = None
y_seed = None

CREATE_FILE = True

def is_vowel(char):
    return char in "aeiouAEIOU"

def main():
    turtle = Turtle()
    turtle.hideturtle()

    turtle.getscreen().setup(SCREEN_SIZE * 1.2, SCREEN_SIZE * 1.2)

    turtle.up()
    tracer(0, 0)

    # horizontal stitches
    turtle.setheading(0)
    for i in range(NUM_CELLS + 1):
        if not SEEDED:
            start = 0 if random() > 0.5 else 1
        else:
            start = y_seed[i % len(y_seed)]
        for j in range(start, NUM_CELLS, 2):
            turtle.setpos(-(SCREEN_SIZE / 2) + j * (SCREEN_SIZE / NUM_CELLS), -(SCREEN_SIZE / 2) + i * (SCREEN_SIZE / NUM_CELLS))
            turtle.down()
            turtle.forward(SCREEN_SIZE / NUM_CELLS)
            turtle.up()

    # vertical stitches
    turtle.setheading(90)
    for i in range(NUM_CELLS + 1):
        if not SEEDED:
            start = 0 if random() > 0.5 else 1
        else:
            start = x_seed[i % len(x_seed)]
        for j in range(start, NUM_CELLS, 2):
            turtle.setpos(-(SCREEN_SIZE / 2) + i * (SCREEN_SIZE / NUM_CELLS), -(SCREEN_SIZE / 2) + j * (SCREEN_SIZE / NUM_CELLS))
            turtle.down()
            turtle.forward(SCREEN_SIZE / NUM_CELLS)
            turtle.up()

    # square border
    turtle.setheading(0)
    turtle.setpos(-SCREEN_SIZE / 2, SCREEN_SIZE / 2)
    turtle.down()
    for i in range(4):
        turtle.forward(SCREEN_SIZE)
        turtle.right(90)

    update()

    if CREATE_FILE:
        filename = 'hitomezashi_' + datetime.now().replace(microsecond=0).isoformat()
        turtle.getscreen().getcanvas().postscript(file=f'{filename}.ps')

    mainloop()