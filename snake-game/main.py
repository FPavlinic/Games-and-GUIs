# used libraries
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# set up the game window
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# create objects important to the game
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# set up controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# play game
game_is_on = True
while game_is_on:
    # update screen
    screen.update()
    time.sleep(0.1)
    # make the snake constantly move
    snake.move()
    # update score
    scoreboard.update_scoreboard()

    # detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall.
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        scoreboard.reset_score()
        snake.reset()

    # detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset()

# keep the game window open until clicked on
screen.exitonclick()
