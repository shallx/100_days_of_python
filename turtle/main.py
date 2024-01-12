from turtle import Turtle, Screen, colormode
# from random_walk import random_walk
from spirograph import drawSpirograph

colormode(255)
t = Turtle()
t.color("red")
screen = Screen()
screen.bgcolor("black")


drawSpirograph(t = t, radius= 100, move = 13, count = 60)

t.screen.mainloop()