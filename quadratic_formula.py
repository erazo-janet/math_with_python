#!/bin/python

#import math function to call the sqrt 
import math
print("Hello, we are going to solve a quadratic equation today.")

#Let the user enter the variables
a = int(input("Enter a number for a: "))
b = int(input("Enter a number for b: "))
c = int(input("Enter a number for c: "))

#calculate the discriminant to determine how many solutions for x there will be
disc = b**2 - 4*a*c

#checking discriminant to find x
if disc > 0 :
    print("There are two real solutions for x")
    x_pos= (-b + math.sqrt(disc))/(2*a)
    print ("x = ", x_pos)
    x_neg = (-b - math.sqrt(disc))/(2*a)
    print ("x = ", x_neg)

if disc == 0 :
    print("There is 1 real solutions for x")
    x_zero = -b/(2*a)
    print("x = ", x_zero)

if disc < 0 :
    print("There is no real solution for x")

