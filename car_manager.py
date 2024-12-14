import turtle as t 
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE = 5
# MOVE_INCREMENT = 10



class CarManager(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.car_speed = 3
        self.rand_generator = 30

    def create_cars(self):
        rand_chance = random.randint(1,self.rand_generator)

        if rand_chance == 1:
            new_car = t.Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.goto(x=320, y=random.randint(-200,250))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.goto(x=car.xcor() - self.car_speed, y=car.ycor())

    def remove(self, car):
        car.hideturtle()
        car.clear()
        self.cars.remove(car)

    def new_level(self):
        self.car_speed += 0.5
        if self.rand_generator > 3:
            self.rand_generator -= 3

