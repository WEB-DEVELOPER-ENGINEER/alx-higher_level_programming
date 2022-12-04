#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = str(number)
for i, j in enumerate(n):
    if i > 0 and n[0] == '-':
        x = -abs(int(n[i]))
    elif i > 0 and n[0] != '-':
        x = int(n[i])
if x > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, x))
elif x == 0:
    print("Last digit of {} is {} and is 0".format(number, x))
elif x < 6 and x != 0:
    print(f"Last digit of {number} is {x} and is less than 6 and not 0")
