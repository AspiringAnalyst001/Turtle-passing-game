from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 270)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score = {self.score}", False, "left", ("italics", 10, "normal"))

    def increase(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, "Center", ("Bold", 20, "normal"))