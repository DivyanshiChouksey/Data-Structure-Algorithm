# Maximum Score After Splitting a String

s = "011101"

def maxScore(s):
    ans = 0
    
    for i in range(len(s) - 1):
        curr = 0
        for j in range(i + 1):
            if s[j] == "0":
                curr += 1
        
        for j in range(i + 1, len(s)):
            if s[j] == "1":
                curr += 1
        
        ans = max(ans, curr)

    return ans



print(maxScore(s))
