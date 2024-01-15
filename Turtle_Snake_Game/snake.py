from turtle import Screen, Turtle
class Snake:
    segments: list[Turtle]  = []
    def __init__(self):
        self.create_snake()

    def create_snake(self):
        '''Create Snake using turtle'''
        for i in range(3):
            t = Turtle("square")
            t.color("white")
            t.penup()
            t.goto(0 - i*20,0)
            self.segments.append(t)

    def move(self):
        '''Move the snake forward each seg linked to other'''
        for i in range(len(self.segments)-1, 0, -1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x, y)
        self.segments[0].forward(20)