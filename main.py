from turtle import Turtle, Screen
from player import Player
from cars import Car
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
cars = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.car_move()
    for car in cars.all_car:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

        if player.final_position():
            scoreboard.increase()
            cars.speed_up()
            player.starting_position()

screen.exitonclick()