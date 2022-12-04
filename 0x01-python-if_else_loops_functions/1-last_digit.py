#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
z = number % 10 if number > 0 else int(repr(number)[-1]) * -1
if (z > 5):
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, z))
elif (z == 0):
    print("Last digit of {:d} is {:d} and is 0".format(number, z))
else:
    print(f"Last digit of {number:d} is {z:d} and is less than 6 and not 0")
