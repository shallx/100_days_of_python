from turtle import Turtle
from constant import CANVAS_HEIGHT, CANVAS_WIDTH, OBJECT_COLOR


class Scoreboard(Turtle):
    l_score = 0
    r_score = 0

    def __init__(self):
        super().__init__()
        self.color(OBJECT_COLOR)
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center",
                   font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center",
                   font=("Courier", 80, "normal"))

    def add_l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def add_r_point(self):
        self.r_score += 1
        self.update_scoreboard()
