# -*- coding: utf-8 -*-
"""
File: palindrome.py
Date:21/10/2016
Author: prashanthisudha kosgi
Course: CSE 7014
Instructor:Nguyen Thai
Description:A simple python program to learn how to program string manipulation.
"""


def isPalindrome(inpstr):
    count = len(inpstr)
    palindrome = True
    i = 0
    while(i < count / 2 + 1):
        if(inpstr[i] != inpstr[count - i - 1]):
            print('kdjd')
            palindrome = False
            break
    i = i + 1

    return palindrome

#test cases
isPalindrome('madam')
isPalindrome('moon')
isPalindrome('Was it a cat I saw')