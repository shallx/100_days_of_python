import random
from turtle import Turtle
from constants import SCREEN_SIZE

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        # self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        pos = int(SCREEN_SIZE/2) - 20
        random_x = random.randint(-pos, pos)
        random_y = random.randint(-pos, pos)

        self.goto(random_x, random_y)