#!/usr/bin/env python3


# A method, greet_programmer() that takes no arguments.
# should output the string "hello, programmer"
def greet_programmer():
    print("Hello, programmer!")

greet_programmer()



# Method greet()
# Takes one argument, a name 
# #should output the string "Hello, name!" with "name" being whatever value was passed as an argument
def greet(name):
      print(f"Hello, {name}!")

greet("Naureen")




# Method great_with_default
# Takes one argument, a name 
# Using default argument  

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default()
greet_with_default("robbie")
    


# method add, takes two numbers as an argument
# returns the sum of the two numbers

def add(num1, num2):
    return num1 + num2

print(add(8,2))




# Method halve 
# Takes two numbers as an argument
# Returns that number's value, divided by two

def halve(num1):
    return num1 / 2

print(halve(100))




    
