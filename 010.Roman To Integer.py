# Roman To Integer
"""
    make a hashmap of roman numerals (consist 7 values only)
    if the value is smaller than the next value it means we subtract samller value
    if the value is greater than the next value it means we add greater value
"""
# Time Complexity = O(n) || Space Complexity = O(1)

s = "MCMXCIV"

def romanToInteger(s):
    roman = {"I":1 , "V":5 , "X":10 , "L":50 , "C":100 , "D":500 , "M":1000}
    res = 0
    for i in range(len(s)):
        if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            res -= roman[s[i]]
        else:
            res += roman[s[i]]
    return res

print(romanToInteger(s))