#  Longest Substring Without Repeating Characters


s = "abcabcbb"


def lengthOfLongestSubstring(self, s: str) -> int:
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
