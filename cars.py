from turtle import Turtle
import random
COLORS = ["red", "blue", "green", "yellow", "orange", "violet"]

DISTANCE = 5
INCREMENT = 10


class Car:
    def __init__(self):
        self.all_car = []
        self.create_car()
        self.car_speed = DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_car.append(new_car)
        
    def car_move(self):
        for cars in self.all_car:
            cars.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += INCREMENT



