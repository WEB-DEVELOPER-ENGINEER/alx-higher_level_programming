#!/usr/bin/python3

Square = __import__('6-square').Square

print("--")
my_square_2 = Square(3, (1, 1))
my_square_2.my_print()
print("--")
my_square_3 = Square(3, (3, "d"))
my_square_3.my_print()
print("--")
try:
    my_square_4 = Square(3)
    my_square_4.position = (0, 0)
except Exception as e:
    print(e)

