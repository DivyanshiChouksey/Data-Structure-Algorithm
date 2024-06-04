# Longest Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        odd, ans = 0, 0
        
        for x in d:
            if d[x] % 2!=0:
                odd += 1
            ans += d[x]

        return min(ans, ans - odd + 1)
