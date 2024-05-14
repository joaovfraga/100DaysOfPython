# Challenge 01 - Drawing a Square:

from turtle import Turtle, Screen

timmy = Turtle()
# timmy.shape("turtle")
timmy.color("grey")

for i in range(4):
    timmy.forward(100)
    timmy.right(90)

screen = Screen()
screen.exitonclick()


