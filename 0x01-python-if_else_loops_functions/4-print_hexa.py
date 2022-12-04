#!/usr/bin/python3
for i in range(99):
    if i == 10 or i == 11 or i == 12 or i == 13 or i == 14 or i == 15:
        j = chr(i + 87)
    elif i < 10:
        j = i
    else:
        j = i - 6
    print(f"{i} = 0x{j}")
