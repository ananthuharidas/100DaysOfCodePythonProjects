from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the game? Enter a color:")
colors = ["red", "blue", "yellow", "green", "orange", "violet"]
y_positions = [-99, -66, -33, 0, 33, 66, 99]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} is the winner.")
            else:
                print(f"You have Lost! The {winning_color} is the winner.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()