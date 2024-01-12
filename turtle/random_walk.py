from turtle import Turtle
import random
def random_walk(t : Turtle, colors):
    t.speed(3)
    t.pensize(4)
    walks = [t.left, t.right, t.back, t.forward]
    for _ in range(60):
        t.color(random.choice(colors))
        movement = random.choice(walks)

        if movement == t.back or movement == t.forward:
            movement(50)
        else:
            movement(90)   
            t.forward(50)
