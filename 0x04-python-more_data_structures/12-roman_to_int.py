#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    total = 0
    num = 0
    digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for r in reversed(roman_string):
        if digits.get(r) is None:
            return 0
        num = digits[r]
        if total >= num * 5:
            num = -num
        total += num
    return total
