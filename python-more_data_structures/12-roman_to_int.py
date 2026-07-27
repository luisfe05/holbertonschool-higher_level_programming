#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    length = len(roman_string)
    for i in range(length):
        val = rom.get(roman_string[i], 0)
        if i + 1 < length and val < rom.get(roman_string[i + 1], 0):
            total -= val
        else:
            total += val
    return total
