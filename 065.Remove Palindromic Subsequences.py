# Remove Palindromic Subsequences
"""
    if string is a palindrome then remove all of it once so the ans = 1
    else we first remove all a's then all b's so the ans = 2
"""
# Time Complexity = O(n) || Space Complexity = O(1)
s = "abb"


def removePalindromeSub(s):
    if len(s) == 0:
        return 0
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:  # not palindrome
            return 2
        i += 1
        j -= 1
    return 1


print(removePalindromeSub(s))
