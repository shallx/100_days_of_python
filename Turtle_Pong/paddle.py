from turtle import Turtle
from constant import OBJECT_COLOR

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.goto(pos)
        self.shape("square")
        self.color(OBJECT_COLOR)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
    
    def go_up(self):
        self.forward(50)
    
    def go_down(self):
        self.backward(50)
        
