from turtle import Turtle
import random
from utils.random_color import random_color

def random_walk(t : Turtle):
    t.speed(3)
    t.pensize(4)
    walks = [t.left, t.right, t.back, t.forward]
    for _ in range(60):
        t.pencolor(random_color())
        movement = random.choice(walks)

        if movement == t.back or movement == t.forward:
            movement(50)
        else:
            movement(90)   
            t.forward(50)
