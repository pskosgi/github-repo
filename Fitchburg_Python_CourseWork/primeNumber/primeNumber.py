
"""
File: primeNumber.py
Date:07/10/2016
Author: prashanthi Sudha kosgi
Course: CSE 7014
Instructor:Nguyen Thai
Description:A simple python program to verify whether a given integer number is a prime number.
"""


def isPrime(num): #Defining isprime function.

 if num <2:  #checking if the num is less than two or not
     print (str(num) + " is not a prime number, def isPrime returns False")
     return False   # Returns false if num is less than 2
 else:
        for i in range(2, num):
            if num % i == 0:  ## see if num is divisible by any number  in the given range.
                print (str(num) + " is not a prime number, def isPrime returns False")
                return False   # Returns false if num is not a prime number
        print (str(num) + " is a prime number, def isPrime returns True")
        return True  # Returns True if num is a prime number, otherwise False.


#testing case's
isPrime(21)
isPrime(29)
isPrime(109)
isPrime(163)
isPrime(227)












