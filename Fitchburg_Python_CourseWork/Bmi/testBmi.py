# -*- coding: utf-8 -*-
"""
File: testBmi.py
Date:14/10/2016
Author: prashanthi sudha kosgi
Course: CSE 7014
Instructor:Nguyen Thai
Description:A simple python program to test the bmi class.
"""
#import BMI class.
from bmi import BMI
def healthStatus(name, age, weight, height): #define healthStatus() method.
    instance = BMI(name, age, weight, height)
    value= instance.getStatus()  #taking result in to value
    print(value) #printing the result.

# input data.
healthStatus('John', 10, 165, 5.9)
healthStatus('Mary', 25, 115, 5.2)
healthStatus('Mark', 60, 135, 5.6)
