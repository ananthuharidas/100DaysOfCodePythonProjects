from turtle import Turtle, Screen
import turtle
import random
tim = Turtle()
tim.shape("turtle")
turtle.colormode(255)
# tim.color("#FF7F50")

# for _ in range(4):
#     for i in range(5):
#         tim.pendown()
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)
#     tim.right(90)

# for num_of_sides in range(3, 11):
#
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
# tim.rght(angle)


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.speed(10)
        tim.width(5)
        tim.pencolor(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)


draw_spirograph(5)

# colors = ["dark orchid", "crimson", "green", "royal blue", "orange", "medium purple"]
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.pen(speed=8)
# for _ in range(200):
#     tim.color(random.choice(colors))
#     tim.forward(30)
#     angle = ["90"]
#     tim.setheading(random.choice(directions))
























screen = Screen()

screen.exitonclick()
