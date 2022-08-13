# Longest Palindrome Substring
"""
    Here we have a naive solution,
    we can make all possible substring of our string and then check every substring is a palindrome or not
    along with store the longest palindromic substring and retrun it. 
"""
# Time Complexity = O(n^3) || Space Complexity = O(n)

string = "abaxyzzyxf"


def longestSubstring(string):
    longest = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i : j + 1]
            if len(substring) > len(longest) and isPalindrome(substring):
                longest = substring
    return longest


def isPalindrome(string):
    l = 0
    r = len(string) - 1
    while l < r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True


print(longestSubstring(string))
