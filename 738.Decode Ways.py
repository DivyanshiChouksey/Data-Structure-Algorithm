# Decode Ways

s = "12"

def numDecodings(s):
    # 226567 = [1,1,2,0,0,0,0]
    if s is None or s[0] == '0':
        return 0
    dp = [0 for i in range(len(s)+1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2,len(s)+1):
        # One step jump
        if 0 < int(s[i-1:i]) <= 9:    #(2)
            dp[i] += dp[i - 1]
        # Two step jump
        if 10 <= int(s[i-2:i]) <= 26: #(3)
            dp[i] += dp[i - 2]
    return dp[-1]


print(numDecodings(s))
