import turtle as turtle_module
import random
tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [ (223, 211, 215), (209, 156, 94), (172, 86, 46), (220, 206, 114), (140, 147, 27), (221, 75, 126), (108, 181, 219), (213, 119, 155), (43, 124, 79), (161, 54, 97), (17, 125, 186), (143, 35, 18), (89, 28, 82), (69, 149, 132), (216, 83, 49), (16, 102, 30), (104, 35, 86), (132, 173, 151), (229, 206, 19), (225, 171, 188), (175, 205, 178), (9, 79, 20), (110, 25, 7), (221, 178, 166), (64, 145, 181), (191, 191, 193), (158, 202, 215)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        



screen = turtle_module.Screen()
screen.exitonclick() 