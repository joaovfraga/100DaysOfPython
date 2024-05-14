import turtle as tm
import random

timmy = tm.Turtle()
tm.colormode(255)

timmy.color("grey")
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

color_list = [(2, 9, 30), (243, 236, 241), (122, 95, 41), (72, 32, 22), (237, 212, 72), (220, 81, 59), (225, 117, 100),
      (93, 1, 21), (178, 140, 170), (150, 92, 115), (34, 90, 26), (7, 154, 73), (205, 63, 91), (168, 129, 77),
      (1, 64, 147), (4, 221, 218), (3, 78, 28), (220, 178, 218), (79, 135, 179), (124, 154, 178), (80, 110, 138),
      (121, 185, 164), (10, 214, 221), (121, 13, 33), (243, 204, 7), (133, 222, 208), (229, 174, 165)]

# Moving the turtle to begin in the place where I want
timmy.setheading(220)
timmy.forward(330)
timmy.setheading(0)

for step1 in range(10):
    for step2 in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)

    for step2 in range(1):
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

# timmy.setheading(90)
# timmy.forward(50)
# timmy.setheading(180)
# timmy.forward(500)
# timmy.setheading(0)


screen = tm.Screen()
screen.exitonclick()




