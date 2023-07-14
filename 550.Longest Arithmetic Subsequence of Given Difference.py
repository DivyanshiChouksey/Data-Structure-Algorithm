# Longest Arithmetic Subsequence of Given Difference

arr = [1,2,3,4]
difference = 1

def longestSubsequence( arr, difference):
    dp = {}
    answer = 1
    for a in arr:
        before_a = dp.get(a - difference, 0)
        dp[a] = before_a + 1
        answer = max(answer, dp[a])
        
    return answer

print(longestSubsequence(arr, difference))
