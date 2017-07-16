# -*- coding: utf-8 -*-
"""
File: shapes.py
Date:21/09/2016
Author: prashanthisudha kosgi
Course: CSE 7014
Instructor:Nguyen Thai
Description:A simple python program to introduce the turtle module.
"""

import turtle
#set up screen
turtle.setup(800,300)      #window size
screen = turtle.Screen()     # instantiate screen class
screen.bgcolor("white")
screen.title("Draw Circles")

#create a ball pen
ballpen = turtle.Turtle()    #Instantiate turtle class
ballpen.pensize(4)

#Draw Triangle
ballpen.color("red")
ballpen.begin_fill()
ballpen.penup()
ballpen.goto(-300, 0)
ballpen.pendown()
ballpen.circle(40, steps=3)
ballpen.end_fill()
ballpen.penup()
ballpen.goto(-350, -50)
ballpen.write("Triangle", font=("Times", 18, "bold"))

#Draw circle
ballpen.color("purple")
ballpen.begin_fill()
ballpen.penup()
ballpen.goto(150, 0)
ballpen.pendown()
ballpen.circle(40)
ballpen.end_fill()
ballpen.penup()
ballpen.goto(130, -50)
ballpen.write("Circle", font=("Times", 18, "bold"))


# Draw Square (4 sides: blue)

ballpen.color("Blue")
ballpen.begin_fill()
ballpen.penup()
ballpen.goto(-200, 0)
ballpen.pendown()
ballpen.circle(40, steps=4)
ballpen.end_fill()
ballpen.penup()
ballpen.goto(-240, -50)
ballpen.write("square", font=("Times", 18, "bold"))

# Draw Pentagon (5 sides: Light Green)

ballpen.color("Light green")
ballpen.begin_fill()
ballpen.penup()
ballpen.goto(-80, 0)
ballpen.pendown()
ballpen.circle(40, steps=5)
ballpen.end_fill()
ballpen.penup()
ballpen.goto(-120, -50)
ballpen.write("Pentagon", font=("Times", 18, "bold"))

# Draw Hexagon (6 sides: Yellow)

ballpen.color("Yellow")
ballpen.begin_fill()
ballpen.penup()
ballpen.goto(30, 0)
ballpen.pendown()
ballpen.circle(40, steps=6)
ballpen.end_fill()
ballpen.penup()
ballpen.goto(10, -50)
ballpen.write("Hexagon", font=("Times", 18, "bold"))

ballpen.color("Light Green")
ballpen.goto(-200, 100)
ballpen.write("Cool Colorful Shapes", font=("Times", 18, "bold"))

#Hide drawing pen
ballpen.hideturtle()
turtle.done()




