import turtle as t

FONT = ("Courier", 20, "normal")



class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.level += 1
        self.goto(x=-225, y=270)
        self.write(f"Level {self.level}", align="center", font=(FONT))