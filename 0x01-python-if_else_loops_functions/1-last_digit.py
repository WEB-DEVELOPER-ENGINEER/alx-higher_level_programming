#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = str(number)
for i, j in enumerate(n):
    if i > 0 and n[0] == '-':
        xe = -abs(int(n[i]))
    elif i > 0 and n[0] != '-':
        xe = int(n[i])
if xe > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, xe))
elif xe == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, xe))
elif xe < 6 and xe != 0:
    print(f"Last digit of {number:d} is {xe:d} and is less than 6 and not 0")
