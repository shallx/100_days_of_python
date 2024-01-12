from turtle import Turtle
def drawMultipleShapes(t : Turtle):
    for i in range(3,8):
        for _ in range(i):
            t.forward(100)
            t.right(360/i)