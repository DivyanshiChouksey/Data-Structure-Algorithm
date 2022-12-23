# Student Attendance Record I

"""
    Iterate through the string and check the conditions 
    the student was absent ('A') for strictly fewer than 2 days total.
    and the student was never late ('L') for 3 or more consecutive days.
    return true if condition are satisfied.
"""

# Time COmplexity = O(n) || Space complexity = O(1)

s = "PPALLL"


def checkRecord(s):
    count = 0
    for i in range(len(s)):
        if s[i] == "A":
            count += 1
        if count >= 2:
            return False
        if i < len(s) - 2 and s[i] == s[i + 1] == s[i + 2] == "L":
            return False

    return True


print(checkRecord(s))
