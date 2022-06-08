# used libraries
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# set up window for the game
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# create necessary objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# set up controls
screen.listen()
screen.onkeypress(player.go_up, "Up")

# play game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()  # update the image in the game window

    car_manager.create_car()  # create cars in the game window
    car_manager.move_cars()  # make the cars move across the game window

    # detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 18:
            game_is_on = False
            scoreboard.game_over()

    # detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()
        car_manager.level_up()

# keep the game window open until cliked on
screen.exitonclick()
