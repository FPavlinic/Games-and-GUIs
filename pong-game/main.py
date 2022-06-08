# used libraries
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# constants
FIELD_WIDTH = 800
FIELD_HEIGHT = 600
FIELD_COLOR = "black"

# set up game field
field = Screen()
field.bgcolor(FIELD_COLOR)
field.setup(FIELD_WIDTH, FIELD_HEIGHT)
field.title("Pong")
field.tracer(0)
field.listen()

# starting positions of paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# set up controls
field.onkeypress(r_paddle.go_up, "Up")
field.onkeypress(r_paddle.go_down, "Down")
field.onkeypress(l_paddle.go_up, "w")
field.onkeypress(l_paddle.go_down, "s")

# create ball and scoreboard objects
ball = Ball()
scoreboard = Scoreboard()

# play game
game_is_on = True
while game_is_on:

    # update screen (depending on speed of the ball)
    time.sleep(ball.move_speed)
    field.update()
    ball.move()

    # detect collision with a wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with a paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect r_paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect l_paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# keep the field on screen until clicked on
field.exitonclick()
