
"""
File: chineseZodiac.py 
Date:30/09/2016
Author: prashanthisudha kosgi
Course: CSE 7014
Instructor:Nguyen Thai
Description:A simple python program calculate the Chinese Zodiac for a given user input as a year number.
"""

import turtle

#Taking input from user and validate for four digits.
a =1    
while  a > 0:
 year=int(input("Enter a year number as an integer :"))
 if year > 999 and year <10000 : break
 else : print(str(year)+" is a invalid year ")
a = a+1

i= year % 12               #calculate zodiac sign

#set up screen
turtle.setup(600,600)           #window size
screen = turtle.Screen()     # instantiate screen class
screen.bgcolor("white")      # instantiate screen color
    

#create a ball pen
ballpen = turtle.Turtle()    #Instantiate turtle class
ballpen.pensize(4)


#Instantiate circle radius.
radius = 200

# Drawing Circle
ballpen.penup()
ballpen.forward(radius)
ballpen.left(90)
ballpen.speed(0)
ballpen.pendown()
ballpen.circle(radius)
ballpen.home()
ballpen.speed(0)
ballpen.right(90)


#Initialising lables.
segment_labels =['Monkey','Rooster','Dog','Pig', 'Rat', 'Ox','Tiger','Rabbit','Dragon','Snake','Horse','Sheep']


#DIviding the circle in to 12 segments.
blocks = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]


#Declaring the co-ordinates for segment lables.
xaxis = [-100, -100, -70, -30, 30, 70, 100, 100, 70, 30, -30, -70]
yaxis = [-30, 30, 70, 100, 100, 70, 30, -30, -70, -100, -100, -70]


#Drawing 12 segments
rollingblock = 0
j=0                          #Initially 0 is assined to j
for block in blocks:         # for loop to draw the segments. 
    
    rollingblock += block
    ballpen.setheading(rollingblock)
    ballpen.speed(0)
    ballpen.position()
    ballpen.pendown()
    ballpen.color("black")   #pen color set to black
    ballpen.forward(radius)
    ballpen.penup()
    ballpen.home()
    j=j+1                   # the value of j is incremented by 1
 
   
# Naming segments
k=0                                      #Initially 0 is assined to k
ballpen1 = turtle.Turtle()               #Instantiate turtle class
for label in segment_labels:             # for loop to writeName the 12 segments
       
    ballpen1.pendown()
    if i==k : ballpen1.pencolor("red")    
    else : ballpen1.pencolor("blue")
    ballpen1.penup()
    ballpen1.goto(xaxis[k], yaxis[k])
    ballpen1.pendown()
    ballpen1.write(segment_labels[k],  align="center", font=("Times", 10, "bold"))
    ballpen1.penup()
    k=k+1  
# Labeling the diagram.
ballpen.color("Black")
ballpen.goto(-180, 250)
ballpen.write('Year to Chinese Zodiac Conversion', font=("Times", 18, "bold"))
ballpen.penup()

#Display of output.
ballpen.goto(-100, -250)
ballpen.write('Year '+str(year)+' is the '+str(segment_labels[i]+'!'), font=("Times", 18, "bold"))
ballpen.penup()

#Hide drawing pen
ballpen.hideturtle()
ballpen1.hideturtle()

turtle.done()
