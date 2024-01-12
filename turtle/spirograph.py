from turtle import Turtle
from utils.random_color import random_color

def drawSpirograph(t : Turtle, radius: int = 90, move: int = 11, count : int = 90):
    t.speed(0)
    for _ in range(count):
        t.pencolor(random_color())
        t.circle(radius)
        t.left(move)