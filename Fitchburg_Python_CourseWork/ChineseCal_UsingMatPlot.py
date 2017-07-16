# -*- coding: utf-8 -*-
"""
File: chineseZodiac.py
Date:21/09/2016
Author: prashanthisudha kosgi
Course: CSE 7014
Instructor:Nguyen Thai
Description:A simple python program to introduce the turtle module.
"""

import matplotlib.pyplot as plot


i =1
while  i > 0:
 yearstring=input("Enter a four digit year number :")
 year = int(yearstring)
 if year > 999 : break
 else : print(str(year)+" is a incorrect year ")
i = i+1
   
  
for i in 'zodiacYear':
  i= year % 12 
      
# Data to plot

plot.title('Year to Chinese Zodiac Conversion.')
labels = ['Monkey','Rooster','Dog','Pig', 'Rat', 'Ox','Tiger','Rabbit','Dragon','Snake','Horse','Sheep']
sizes = [30,30,30,30,30,30,30,30,30,30,30,30]
colors = ['blue', 'blue', 'blue', 'blue','blue','blue','blue','blue', 'blue', 'blue', 'blue','blue','blue','blue']
colors[i]='red'
plot.text(0.1,-1.1 , 'Year '+str(year)+ ' is the '+ labels[i] + '!' , fontsize=12)
 
# Plot
plot.pie(sizes, labels=labels,labeldistance=0.7,counterclock=False, colors=colors,shadow=False, startangle=90)
 
plot.axis('equal')
plot.show()