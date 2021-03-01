import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(key="Up", fun=player.move_forward)
cars = []
game_is_on = True
cycle = 0
CAR_SPEED = 10
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cycle += 1
    if cycle > 6:
        car = CarManager()
        cars.append(car)
        cycle = 0

    for c in cars:
        c.move(CAR_SPEED)
        if c.distance(player) < 20:
            game_is_on = scoreboard.game_over()
        if c.xcor() < -300:
            c.hideturtle()
            cars.remove(c)

    if player.ycor() > 260:
        player.goto(player.start_position)
        CAR_SPEED += 2
        scoreboard.level_up()
        # game_is_on = scoreboard.game_over()

screen.exitonclick()