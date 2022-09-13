# Longest Substring without Repeating character

"""
    Using slinding window approach
    take 2 pointers i and j both are initially at the starting point of string S and keep record of max length of substring
    create a hashmap to store frequencies of characters and 
    iterate through the string with pointer j from i+1 indices to len(string)
    and if found any repeated character then increase i pointer by 1 and update max length if the current substring length is greater
    after that return max length of substring.

"""
s = "abcabcbb"


def lengthOfLongestSubstring(s):
    i, j = 0, 0
    maxLen = 0
    count = {}
    # a:1
    while j < len(s):
        if s[j] not in count:
            count[s[j]] = 0

        count[s[j]] += 1

        while count[s[j]] > 1:
            count[s[i]] -= 1
            i += 1
        j += 1
        maxLen = max(maxLen, j - i)
    return maxLen


print(lengthOfLongestSubstring(s))
