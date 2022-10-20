# Integer to Roman

"""
    Make a 2D array containing value and roman numerals 
    go through the array in reverse order so that we start with largest value then
    divided num with largest value and update num with mod of largest value and add 
    divided times roman in ans.

        ans = MMMMMV
        num = 5005
        5000//1000 => 5
        5000%1000 -> 5
        5//5 -> 1
        5%5 = 0
        
        num = 900
        900//1000-> 0
        900//900 -> 1
"""
# Time Complexity = O(1) || Space Complexity = O(n)

num = 1994


def intToRoman(num: int) -> str:
    roman = [
        [1, "I"],
        [4, "IV"],
        [5, "V"],
        [9, "IX"],
        [10, "X"],
        [40, "XL"],
        [50, "L"],
        [90, "XC"],
        [100, "C"],
        [400, "CD"],
        [500, "D"],
        [900, "CM"],
        [1000, "M"],
    ]

    ans = ""
    for val, rom in roman[::-1]:
        tmp = num // val
        num %= val
        ans += tmp * rom
        if num == 0:
            return ans


print(intToRoman(num))
