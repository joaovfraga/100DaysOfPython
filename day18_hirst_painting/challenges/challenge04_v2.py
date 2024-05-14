# Challenge 04 - Drawing Random Walk V2:

import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)

timmy.shape("turtle")
timmy.pensize(15)
timmy.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    y = random.randint(0, 255)
    g = random.randint(0, 255)
    new_random_color = (r, y, g)
    return new_random_color


directions = [0, 90, 180, 270]

for steps in range(200):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
