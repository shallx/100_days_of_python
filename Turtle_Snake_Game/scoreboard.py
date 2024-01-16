from turtle import Turtle
from constants import SCREEN_SIZE, SCOREBOARD_ALIGMENT, SCOREBOARD_FONT

class Scoreboard(Turtle):
    score = 0
    high_score = 0
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(0, SCREEN_SIZE//2 - 30)
        self.high_score = self.read_highscore()
        self.rewrite_score()

    def increase_score(self):
        self.score += 1
        self.rewrite_score()

    def rewrite_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=SCOREBOARD_ALIGMENT, font=SCOREBOARD_FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.update_highscore(self.score)
        self.score = 0
        self.rewrite_score()

    def read_highscore(self):
        with open("data.txt", mode="r+") as file:
            if file.read() == '':
                file.write("0")
            file.seek(0)
            score = int(file.read())
        return score

    def update_highscore(self, score):
        self.high_score = score
        with open("data.txt", mode="w") as file:
            file.write(f"{score}")

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=SCOREBOARD_ALIGMENT, font=SCOREBOARD_FONT)
