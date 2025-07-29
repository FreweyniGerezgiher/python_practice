import turtle as t
from turtle import Screen
import random 
tim = t.Turtle()

colours = ["red", "green", "blue", "DarkOrchid", "DeepSkyBlue", "IndianRed", "Wheat"]
# n = 3

# while n < 10 :
    
#     for _ in range(n):
#         tim.forward(100)
#         tim.left(360/n) 
#     n += 1

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)
    



screen = Screen()
screen.exitonclick()  