# used libraries
import random
import turtle

tim = turtle.Turtle()  # create Turtle object
tim.speed("fastest")  # set speed
my_screen = turtle.Screen()  # create screen
my_screen.colormode(255)  # set colormode

# list of colors used in painting
color_list = [(211, 154, 97), (52, 107, 132), (176, 78, 34), (200, 142, 33), (116, 155, 171), (124, 79, 98), (122, 175, 157), (229, 197, 128), (190, 88, 109), (55, 38, 19), (11, 51, 65), (44, 168, 125), (197, 122, 141), (50, 125, 120), (167, 21, 29), (225, 94, 80), (244, 162, 160), (4, 28, 26), (38, 32, 34), (80, 148, 170), (162, 26, 21), (236, 165, 170), (98, 125, 160), (167, 207, 192), (22, 79, 91), (162, 203, 212)]

x = -250
y = -250
tim.hideturtle()  # hide turtle from screen
tim.penup()  # lift pen up --> not drawing
tim.setpos(x, y)  # move to starting position

for row in range(10):  # go through 10 columns
    for column in range(10):  # go through 10 rows
        tim.dot(20, random.choice(color_list))  # draw dots size 20
        tim.penup()  # lift pen to stop drawing
        tim.forward(50)  # move by 50
    y += 50  # when row is finished jump to next row
    tim.goto(x, y)  # new starting position X = X but Y = Y + 50 (next row)

my_screen.exitonclick()  # keep screen open until clicked on

# code below can be used to extract colors from image
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     rgb_colors.append(tuple(color.rgb))
#
# print(rgb_colors)
