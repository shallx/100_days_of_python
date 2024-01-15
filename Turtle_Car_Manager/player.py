STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def did_reach_top(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
        
    def level_up(self):
        self.goto(STARTING_POSITION)
