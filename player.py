from turtle import Turtle
MOVE_DISTANCE = 10
STARTING_POSITION = (0, -280)
FINISHING_LINE =280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.left(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.move_up()

    def move_up(self):
        new_ycor = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_ycor)

    def move_down(self):
        new_ycor = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_ycor)

    def starting_position(self):
        self.goto(STARTING_POSITION)

    def final_position(self):
        if self.ycor() > FINISHING_LINE:
            return True
        else:
            return False
