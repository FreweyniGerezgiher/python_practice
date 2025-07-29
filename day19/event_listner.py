from turtle import Turtle
from turtle import Screen

tim = Turtle()

def move_forwards():
    tim.forward(10)

def move_backward():
    tim.back(10)

def move_right():
    tim.right(10)


def move_left():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
       


screen = Screen()
screen.listen()
#def select_key():
screen.onkey(key = "w", fun= move_forwards)
screen.onkey(key = "s", fun= move_backward)
screen.onkey(key = "r", fun= move_right)
screen.onkey(key = "l", fun= move_left)
screen.onkey(key = "c", fun= clear )
#select_key()
clear()
screen.exitonclick()