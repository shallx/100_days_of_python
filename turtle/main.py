from turtle import Turtle, Screen, colormode
from random_walk import random_walk

colormode(255)
t = Turtle()
t.color("red")
screen = Screen()
screen.bgcolor("black")


random_walk(t)

t.screen.mainloop()