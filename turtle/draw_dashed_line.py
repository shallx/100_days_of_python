from turtle import Turtle
def drawDashedLine(t : Turtle):
    for i in range(20):
        t.forward(10)
        if i % 2 == 0:
            t.up()
        else:
            t.down()