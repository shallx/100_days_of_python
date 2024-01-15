from turtle import Turtle
from constant import OBJECT_COLOR, CANVAS_WIDTH, CANVAS_HEIGHT

class Ball(Turtle):
    moveX = 10
    moveY = 10
    def __init__(self):
        super().__init__("circle")
        self.color(OBJECT_COLOR)
        self.penup()

    def move(self):
        self.goto(self.xcor() + self.moveX, self.ycor() + self.moveY)

    def didCollide(self):
        if self.xcor() > CANVAS_WIDTH//2 -20 or self.xcor() < -(CANVAS_WIDTH//2 -20):
            self.moveX *= -1
        elif self.ycor() > CANVAS_HEIGHT//2 -20  or self.ycor() < -(CANVAS_HEIGHT//2 -20):
            self.moveY *= -1

        