# Is Subsequence

# Time COmplexity = O(n) || Space Complexity = O(1)

s = "bcd"
t = "uuuubcd"


def isSubsequence(s, t):
    if len(s) == 0:
        return True
    i = 0
    for char in t:
        if s[i] == char:
            i += 1
            if i == len(s):
                return True
    return False


def isSubsequence2(s, t):
    if len(s) == 0:
        return True
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        if i == len(s):
            return True
        else:
            j += 1

    return False


print(isSubsequence(s, t))
print(isSubsequence2(s, t))
