import turtle as t

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(x=0, y=-270)

    def move_forward(self):
        self.forward(15)

    def move_backwards(self):
        self.backward(15)

    def reset(self):
        self.goto(x=0, y=-270)
