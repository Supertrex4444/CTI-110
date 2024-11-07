#Travis Cayton
#11/7/2024
#P4LAB1
#Draw a square and triangle using turtle library

import turtle

win = turtle.Screen()
t = turtle.Turtle()

win.bgcolor("black")

t.pensize(8)
t.pencolor("blue")
t.shape("arrow")

num = 0

while num < 4:
    t.forward(150)
    t.left(90)
    num = num + 1
    
t.left(90)
t.forward(150)
t.right(90)
for i in range(0,3):
    t.forward(150)
    t.left(120)
