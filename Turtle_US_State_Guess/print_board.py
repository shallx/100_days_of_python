from turtle import Turtle

class PrintBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()

    
    def write_state(self, pos, state):
        self.goto(pos)
        self.write(f"{state}", align="center", font=("Courier", 12, "normal"))