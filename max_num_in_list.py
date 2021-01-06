#!/bin/python

#Specify an empty list. We will append user input into this list 
st = []

#check how big our range will be
num_list = int(input("How many numbers are you going to list?: "))

#Run the for loop until the number entered for num_list is reached 
for n in range (num_list): 
    numbers = int(input("Enter a number: "))
    st.append(numbers)

    # append is used to add the numbers entered by the user into the empty list, st

print("The maximum number is", max(st))

