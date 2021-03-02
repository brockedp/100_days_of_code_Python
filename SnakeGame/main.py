import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import  Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        if scoreboard.score % 10 == 0:
            snake.increase_speed()

    # Detect collison with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        snake.reset()
        scoreboard.reset()

    # Detect with collison with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset()


screen.exitonclick()
