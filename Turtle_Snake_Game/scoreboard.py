from turtle import Turtle
from constants import SCREEN_SIZE, SCOREBOARD_ALIGMENT, SCOREBOARD_FONT

class Scoreboard(Turtle):
    score = 0
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.rewrite_score()

    def increase_score(self):
        self.score += 1
        self.rewrite_score()

    def rewrite_score(self):
        self.clear()
        self.goto(0, SCREEN_SIZE//2 - 30)
        self.write(f"Score: {self.score}", align=SCOREBOARD_ALIGMENT, font=SCOREBOARD_FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=SCOREBOARD_ALIGMENT, font=SCOREBOARD_FONT)
