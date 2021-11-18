# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 21:25:14 2021

Day 1 of the 100 Days Python Challenge

@author: omerf
"""

"""
Day 1 
Execise 1

Make the output of your program match the given output below:

Day 1 - Python Print Function
The function is declared like this:
print('what to print')

"""
# Solution to Execise 1
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")


"""
Day 1
Execise 2

Write a program that prints the number of characters in a user's name.

"""

# Solution to Execise 2
print(len(input("What is your name?")))


"""
Day 1
Execise 3

Write a program that switches the values stored in the variables a and b.

a = input("a: ")
b = input("b: ")

####################################
#Write your code below this line


#Write your code above this line
####################################

print("a: " + a)
print("b: " + b)

"""

# Solution to Execise 3
a = input("a: ")
b = input("b: ")

c = b
b = a
a = c

print("a: " + a)
print("b: " + b)
