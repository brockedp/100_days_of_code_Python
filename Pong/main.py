from turtle import Screen
from scoreboard import Scoreboard
from player import Player
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Pong Pong")
screen.tracer(0)
scoreboard = Scoreboard()
player_one = Player((-350, 0))
player_two = Player((350, 0))
ball = Ball()
screen.update()
screen.listen()

def game_over():
    return False

screen.onkeypress(key="w", fun=player_one.move_up)
screen.onkeypress(key="s", fun=player_one.move_down)
screen.onkeypress(key="Up", fun=player_two.move_up)
screen.onkeypress(key="Down", fun=player_two.move_down)

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.hit_y()
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.hit_x()

    if ball.xcor() > 370:
        scoreboard.increase_score(1)
        ball.ball_speed = ball.ball_start_speed
        ball.reset_positon()

    if ball.xcor() < -370:
        scoreboard.increase_score(2)
        ball.ball_speed = ball.ball_start_speed
        ball.reset_positon()


    if ball.distance(player_one) < 50 and ball.xcor() < -330 or ball.distance(player_two) < 50 and ball.xcor() > 330:
        print("made contact")
        ball.hit_x()
        if ball.ball_speed > 0:
            ball.ball_speed -= 0.01

    if scoreboard.player_one_score > 9:
        game_on = False
        scoreboard.display_winner(1)
    if scoreboard.player_two_score > 9:
        game_on = False
        scoreboard.display_winner(2)


screen.exitonclick()