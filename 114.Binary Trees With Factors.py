# Binary Trees With Factors
from collections import defaultdict


arr = [2, 4]
arr.sort()
dp = defaultdict(int)
for i,cur_num in enumerate(arr)):
    for j in range(i):
        factor = arr[j]
        quotient, remainder = divmod(arr[i], factor)
        # quotient = arr[i]//arr[j]
        # remainder = arr[i]%arr[j]
        if remainder == 0:
            dp[cur_num] += dp[quotient] * dp[factor]
            # dp[arr[i]] += dp[quotient] * dp[remainder]
    dp[arr[i]] += 1
