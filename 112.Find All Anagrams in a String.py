# Find All Anagrams in a String
"""
    Create a counter for p string and go through the s string for n - m + 1  ie(len(s)-len(p)+1) times
    construct a window of len(p) size in S string and then create another counter of that window after that compare,
    if both counters are equal then add the index of S string in our ans or
    else remove the very first element of the window and add next element of S string to that window by this we'll maintain the size of the window
"""

# Time Complexity = O(n),  n = len(s)
# Space Complexity = O(m), m = len(p)


s = "cbaebabacd"
p = "abc"


from typing import Counter


def findAnagrams(s, p):
    n = len(s)
    m = len(p)
    ans = []
    p = Counter(p)

    for i in range(n - m + 1):
        if i == 0:
            count = Counter(s[:m])
        else:
            count[s[i - 1]] -= 1
            count[s[i + m - 1]] += 1

        if p == count:
            ans.append(i)

    return ans


print(findAnagrams(s, p))
