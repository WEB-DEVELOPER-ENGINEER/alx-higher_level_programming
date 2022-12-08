#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        l = len(roman_string)
        for i in range(len(roman_string)):
            if i + 1 < l and roman[roman_string[i]] < roman[roman_string[i+1]]:
                res -= roman[roman_string[i]]
            else:
                res += roman[roman_string[i]]
        return res
    else:
        return 0
