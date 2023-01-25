# Substrings of Size Three with Distinct Characters
s = "aababcabc"

"""
    Going through the string and take 3 values from current at a time after that if each character 
    is distinct in that 3 values then increase our ans by 1 and move our current to next 
"""

# Time Complexity = O(n) || Space Complexity = O(1)


def countGoodSubstrings1(s):
    ans = 0
    for i in range(2, len(s)):
        if s[i] != s[i - 1] and s[i] != s[i - 2] and s[i - 1] != s[i - 2]:
            ans += 1
    return ans


"""
    Using sliding window concept
"""

# Time Complexity = O(n) || Space Complexity = o(1)


def countGoodSubstrings2(s):
    i = 0
    ans = 0
    while i < len(s) - 2:
        j = i
        seen = set()
        while j < i + 3 and s[j] not in seen:
            seen.add(s[j])
            j += 1
        if j == i + 3:
            ans += 1
        i += 1
    return ans


print(countGoodSubstrings1(s))
print(countGoodSubstrings2(s))
