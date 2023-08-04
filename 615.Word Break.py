# Word Break

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]


# Optimized Solution
def wordBreak(s, wordDict):
    dp = [False] * len(s)
    for i in range(len(s)):
        for word in wordDict:
            if i < len(word) - 1: # Handle out of bounds case
                continue
            
            if i == len(word) - 1 or dp[i - len(word)]:
                if s[i - len(word) + 1:i + 1] == word:
                    dp[i] = True
                    break

    return dp[-1]

print(wordBreak(s, wordDict))


# Naive Solution
def wordBreak(s, wordDict):
    """
        l e e t c o d e    leet, code
      1 0 0 0 1 0 0 0 1  
    """
    dp = [0]*(len(s)+1)
    dp[0] = 1
    for i in range(1,len(dp)):
        for j in range(0,i):
            if s[j:i] in wordDict and dp[j]:
                dp[i] = 1
    return False if dp[-1] ==0 else True
    # return dp[-1]  can also use this 

print(wordBreak(s, wordDict))