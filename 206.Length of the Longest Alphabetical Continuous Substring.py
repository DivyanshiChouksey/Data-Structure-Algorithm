# Length of the Longest Alphabetical Continuous Substring

s = "abacaba"


def longestContinuousSubstring(self, s: str) -> int:
    alpha = "abcdefghijklmnopqrstuvwxyz"
    maxLen = 0
    i = 0
    while i < len(s):
        j = i
        t = ord(s[i]) - 97
        while t < 26 and j < len(s) and s[j] == alpha[t]:
            t += 1
            j += 1
        maxLen = max(maxLen, j - i)
        i += 1

    return maxLen
