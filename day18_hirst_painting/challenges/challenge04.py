# Challenge 04 - Drawing Random Walk:

from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.pensize(15)
timmy.speed("fastest")

colors = ["CornFLowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen",
          "Gold", "DeepPink", "SaddleBrown", "Chartreuse", "Navy", "grey", "Goldenrod", "Firebrick", "OliveDrab"]
directions = [0, 90, 180, 270]

for steps in range(200):
    timmy.color(random.choice(colors))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()