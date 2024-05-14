# Challenge 05 - Drawing a Spirograph:

import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    y = random.randint(0, 255)
    g = random.randint(0, 255)
    color = (r, y, g)
    return color


timmy.speed("fastest")


def draw_spirograph(size_of_gap):
    for steps in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(20)

screen = Screen()
screen.exitonclick()
