# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 22:48:56 2021

Day 3 of the 100 Days Python Challenge

@author: omerf
"""

"""
Day 3
Exercise 1

Write a program that works out whether if a given number is an odd or even number.
"""

number = int(input("Which number do you want to check? "))

if number%2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
    

"""
Day 3
Exercise 2

Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
It should tell them the interpretation of their BMI based on the BMI value.

-Under 18.5 they are underweight
-Over 18.5 but below 25 they have a normal weight
-Over 25 but below 30 they are slightly overweight
-Over 30 but below 35 they are obese
-Above 35 they are clinically obese.
"""

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(int(weight) / (float(height)**2))

if bmi < 18.5:
    print(f"Your BMI is {int(bmi)}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {int(bmi)}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {int(bmi)}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {int(bmi)}, you are obese.")
else:
    print(f"Your BMI is {int(bmi)}, you are clinically obese.")
    

"""
Day 3
Exercise 3

Write a program that works out whether if a given year is a leap year. 
A normal year has 365 days, leap years have 366, with an extra day in February. 

This is how you work out whether if a particular year is a leap year.
on every year that is evenly divisible by 4 
**except** every year that is evenly divisible by 100 
**unless** the year is also evenly divisible by 400
"""

year = int(input("Which year do you want to check? "))

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")


"""
Day 3
Exercise 4

Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.

Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25

Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
"""

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


final_bill = 0

if size == 'S':
    final_bill = final_bill + 15
elif size =='M':
    final_bill = final_bill + 20
elif size =='L':
    final_bill = final_bill + 25

if add_pepperoni == 'Y':
    if size == 'S':
        final_bill = final_bill + 2
    else:
        final_bill = final_bill + 3

if extra_cheese == 'Y':
    final_bill = final_bill + 1

print(f"Your final bill is: ${final_bill}.")


"""
Day 3
Exercise 5

You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. 
Then combine these numbers to make a 2 digit number.
"""

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name_combined = name1.lower() + name2.lower()

counter_true = 0
for i in name_combined:
    if i in "true":
        counter_true += 1 

counter_love = 0
for i in name_combined:
    if i in "love":
        counter_love += 1 
       
total_score = str(counter_true) + str(counter_love)

total_score = int(total_score)
if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif 40 < total_score < 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")


