# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 02:22:09 2021

Day 2 of the 100 Days Python Challenge

@author: omerf
"""

"""
Day 2 
Execise 1

Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, 
then the output should be 3 + 5 = 8

"""

# Solution to Execise 1
two_digit_number = input("Type a two digit number: ")
print(int(two_digit_number[0]) + int(two_digit_number[1]));

"""
Day 2 
Execise 2

Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
Warning you should convert the result to a whole number.    

"""

# Solution to Execise 2
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight) / (float(height)**2)
print(int(bmi))

"""
Day 2 
Execise 3

Create a program using maths and f-Strings that tells us how many days, weeks, months we have left 
if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
You have x days, y weeks, and z months left.

"""

age = input("What is your current age?")

age_until_ninety = 90 - int(age)

print(f"You have {age_until_ninety*365} days, {age_until_ninety*52} weeks, and {age_until_ninety*12} months left.")
