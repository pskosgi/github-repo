"""
File: bmi.py
Date:14/10/2016
Author: prashanthi sudha kosgi
Course: CSE 7014
Instructor:Nguyen Thai
Description:A simple python program to implement the body mass index (BMI) class.
"""
class BMI:   #creating BMI class
#constructor is created with parameters.
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
#Defining getBMI() method.
    def getBMI(self):
        #Formula to calculate BMI value
            return self.weight * 0.45359237 /((self.height *0.3048 ) * (self.height*0.3048))
#Defining getStatus() method.
    def getStatus(self):
        if self.age<16:  #checking for age.
            return "Please enter age 16 or above for user:"+self.name
        else:
            bmi = self.getBMI()
            if bmi < 18.5:
                return "Underweight"
            elif bmi >= 18.5 and bmi <= 24.9:
                return "Normalweight"
            elif bmi >= 25 and bmi <= 29.9:
                return "Overweight"
            elif bmi >= 30:
                return "Obese"