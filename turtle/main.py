from turtle import Turtle, Screen
from random_walk import random_walk

t = Turtle()
t.color("red")
screen = Screen()
screen.bgcolor("black")

colors = ["blue", "red", "salmon", "green", "purple", "yellow"]

random_walk(t, colors)

t.screen.mainloop()