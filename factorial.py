#!/bin/python
#  A factorial of a positive integer n, denoted by n! is the prodcut of all positive integers less than or equal to n
# To calculate factorial: n! = n(n-1)!
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

#Recieve user input 
n = int(input("Enter a number: "))
result = factorial(n)
print(n, "factorial is", result)
