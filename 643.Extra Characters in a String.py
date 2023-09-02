# Extra Characters in a String

# Time : O(n^3)
# Space : O(n)

s = "sayhelloworld"
dictionary = ["hello","world"]


def minExtraChar(s,dictionary):
    max_val = len(s) + 1
    dp = [max_val] * (len(s) + 1)
    dp[0] = 0 
    dictionary_set = set(dictionary)

    for i in range(1, len(s) + 1):
        dp[i] = dp[i - 1] + 1

        for l in range(1, i + 1): 
            
            if s[i-l:i] in dictionary_set:
                dp[i] = min(dp[i], dp[i-l])
                
    return dp[-1]

print(minExtraChar(s,dictionary))
