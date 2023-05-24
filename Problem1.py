#!/usr/bin/python3
number = 100
# Your code should be below this line

#creates first numbers of fibonacci sequence
num1 = 0
num2 = 1

#finds the sum of the 2 numbers, which is the next num
sum = num1 + num2

#loop iterates until target is reached
while sum < number:
    #finds next number in sequence
    num1 = num2
    num2 = sum
    sum = num1 + num2

#checks if the fibonacci number is equal to target and is even
if (sum == number) and (number % 2 == 0):
    print("Yes")
else:
    print("No") 