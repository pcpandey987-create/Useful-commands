#!/usr/bin/env python3
import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Spiral")

t = turtle.Turtle()
t.speed(0)
turtle.tracer(2)
t.hideturtle()

hue = 0.0

for i in range(1500):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    t.pencolor(color)
    t.forward(i * 0.2)
    t.right(100)
    hue += 0.006

t.up()
t.goto(0, -320)
t.color("white")
t.write("💗", align="center", font=("arial", 36, "bold"))

turtle.done()
