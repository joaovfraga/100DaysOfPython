# Challenge 02 - Drawing a Dashed Line:

from turtle import Turtle, Screen

timmy = Turtle()
# timmy.shape("turtle")
timmy.color("grey")

for steps in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen = Screen()
screen.exitonclick()