#!/usr/bin/python3
n = 21
# Your code should be below this line

#checks if day is saturday or sunday
if (n % 7 == 1) or (n % 7 == 2):
    print("Weekend")
else:
    print("Weekday")

