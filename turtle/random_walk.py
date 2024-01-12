from turtle import Turtle
import random
from utils.random_color import random_color

def random_walk(t : Turtle):
    t.speed(10)
    t.pensize(4)
    for _ in range(100):
        t.pencolor(random_color())
        movement(t)
            
def movement(t : Turtle, steps: int = 50):
    t.forward(steps)
    t.setheading(random.choice([0, 90, 180, 270]))