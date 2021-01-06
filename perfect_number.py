#!/bin/python

#In number theory, a perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the integer itself


n = int(input("Enter any number: "))
sum = 0

# For loop is used to calculate all divisors of the number n entered by the user, and sum the divisors to check if it equals n
for i in range(1, n):
    #This calculates the divisors of n, and sums all diviors together until all divisors have been added 
    if(n % i == 0):
        sum = sum + i

# Condition to check if the sum of n divisors equals n
if (sum == n):
    print(n, "is a Perfect number!")
else:
    print(n, "is not a Perfect number!")

