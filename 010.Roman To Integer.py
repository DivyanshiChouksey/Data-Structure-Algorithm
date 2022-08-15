# Roman To Integer
"""
    Create a hashmap of roman numerals (consist 7 values only) and initialize a variable to store current sum
    if the value is smaller than the next value it means we have to subtract value from stored sum and 
    if the value is greater than or equals to the next value it means we have to add value from stored sum
    and keep in mind to always add the last value.
"""
# Time Complexity = O(n) || Space Complexity = O(1)

s = "MCMXCIV"


def romanToInteger(s):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            res -= roman[s[i]]
        else:
            res += roman[s[i]]
    return res


print(romanToInteger(s))
