import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True
screen.listen()
screen.onkey(fun=player.move_up, key="Up")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.spawn_car()
    car_manager.move_car()

    # Detect collision with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect a successful crossing
    if player.is_player_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
