# Challenge 03 - Drawing Different Shapes:

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("grey")

# My Solution

# triangle
for step in range(3):
    timmy.right(120)
    timmy.forward(100)
# square
timmy.color("red")
for step in range(4):
    timmy.right(90)
    timmy.forward(100)
# pentagon
timmy.color("MidnightBlue")
for step in range(5):
    timmy.right(72)
    timmy.forward(100)
# hexagon
timmy.color("Gold")
for step in range(6):
    timmy.right(60)
    timmy.forward(100)
# heptagon
timmy.color("DarkViolet")
for step in range(7):
    timmy.right(360 / 7)
    timmy.forward(100)
# octagon
timmy.color("ForestGreen")
for step in range(8):
    timmy.right(360 / 8)
    timmy.forward(100)
# nonagon:
timmy.color("Black")
for step in range(9):
    timmy.right(360 / 9)
    timmy.forward(100)
# decagon
timmy.color("DarkOrange")
for step in range(10):
    timmy.right(360 / 10)
    timmy.forward(100)

screen = Screen()
screen.exitonclick()
