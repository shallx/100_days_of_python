FONT = ("Courier", 24, "normal")

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-260, 260)
        self.level = 1
        self.print_level()
        

    def print_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Courier", 18, "normal"))

    
    def game_over(self):
        self.home()
        self.write(f"Game Over", align="center", font=("Courier", 24, "normal"))

    def level_up(self):
        print("leveling up")
        self.level += 1
        self.print_level()

