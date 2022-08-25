# Minimum Deletions to Make Character Frequencies Unique
"""
    Store frequencies of character of S string with the help of counter in a reverse order,
    initialise a variable to store no. of min deletions and a maxFreq initially len(S) after that
    if freq is greater than maxFreq then add freq-maxfreq nos. of deletion or else update freq with freq-1
    and then repeat this until we got unique frequencies of characters.
"""
# Time Complexity = O(n) || Space Complexity = O(n)

s = "abcabc"


from typing import Counter


def minDeletions(s):
    c = Counter(s)
    freq = []
    for k, v in c.items():
        freq.append(v)
    freq.sort(reverse=True)
    delCount = 0
    maxFreq = len(s)
    for f in freq:
        if f > maxFreq:
            delCount += f - maxFreq
            f = maxFreq
        maxFreq = max(0, f - 1)
    return delCount


# Solution2
def minDeletions2(s) -> int:
    frequencies = [0] * 26
    for char in s:
        frequencies[ord(char) - ord("a")] += 1
    frequencies.sort(reverse=True)
    maxFreq = len(s)
    count = 0
    for f in frequencies:
        if f == 0:
            break
        if f > maxFreq:
            count += f - maxFreq
            f = maxFreq
        maxFreq = max(f - 1, 0)
    return count


print(minDeletions(s))
print(minDeletions2(s))
