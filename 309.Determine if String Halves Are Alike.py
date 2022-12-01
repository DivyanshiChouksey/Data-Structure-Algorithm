# Determine if String Halves Are Alike

"""
    Taking two variables ans1 and ans2 to keep record of number of times vowels occurs, 
    go through the half of string S then check if character of s is in the string "aeiouAEIOU"
    then increase the ans1 by 1 similarly then go through the remaining half of string and check character of s is
    in the string "aeiouAEIOU" then increase ans2 by 1 at the end return True if both ans1 and ans2 are equal 
    otherwise False.
"""

# Time Complexity = O(n) || Space Complexity = O(1)

from collections import Counter

s = "textbook"


def halvesAreAlike(s):
    ans = 0
    for n in range(len(s) // 2):
        if s[n] in "aeiouAEIOU":
            ans += 1

    ans2 = 0
    for m in range(len(s) // 2, len(s), 1):
        if s[m] in "aeiouAEIOU":
            ans2 += 1

    return ans == ans2


print(halvesAreAlike(s))
