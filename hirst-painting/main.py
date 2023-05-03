"""Extract colours from an jpeg image using colorgram."""
# import colorgram
# colors = colorgram.extract('image.jpeg', 80)
# rgb_color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color_list.append((r, g, b))
# print(rgb_color_list)

import turtle as turtle_module
import random
turtle_module.colormode(255)
tim = turtle_module.Turtle()
colors = [(241, 217, 71), (236, 151, 68), (41, 104, 152), (219, 157, 6), (106, 178, 214), (178, 15, 47), (236, 47, 79), (187, 80, 20), (31, 188, 126), (224, 129, 143), (226, 217, 4), (245, 60, 31), (66, 29, 55), (243, 159, 185), (159, 54, 84), (98, 105, 192), (109, 201, 161), (134, 228, 187), (34, 48, 134), (158, 27, 18), (122, 217, 238), (33, 34, 72), (36, 140, 90), (27, 178, 198), (26, 86, 79), (236, 169, 161), (93, 26, 13), (10, 92, 107), (253, 5, 36), (167, 190, 226), (18, 64, 58), (101, 76, 20), (254, 11, 2)]
tim.penup()
tim.hideturtle()
tim.setposition(-250, -250)
number_of_dots = 100
tim.speed("fastest")
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen = turtle_module.Screen()
screen.exitonclick()