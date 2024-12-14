import time
import turtle as t
import car_manager
import scoreboard
import player

screen = t.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = player.Player()
car_manager = car_manager.CarManager()
scoreboard = scoreboard.Scoreboard()

screen.listen()
screen.onkey(fun=player.move_forward, key="Up")
screen.onkey(fun=player.move_backwards, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(0.025)
    screen.update()
    car_manager.create_cars()
    car_manager.move()

    #delete cars off the screen
    for car in car_manager.cars:
        if car.xcor() < -320:
            car_manager.remove(car)

    #check collison
    for car in car_manager.cars:
        # if ((car.xcor() - 10 < player.xcor() < car.xcor() + 10) and (car.ycor() -20 < player.ycor() < car.ycor() + 20)):
        if player.distance(car) < 20:
            game_is_on = False

    if player.ycor() > 270:
        scoreboard.update_score()
        player.reset()
        car_manager.new_level()

game_over = t.Turtle()
game_over.color("Red")
game_over.write("GAME OVER", align="center", font=("Courier", 36, "normal"))

screen.exitonclick()