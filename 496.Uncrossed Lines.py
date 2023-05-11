# Uncrossed Lines

nums1 = [2,5,1,2,5]
nums2 = [10,5,2,1,5,2]

def maxUncrossedLines(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)

    dp = [0] * (n2 + 1)
    dpPrev = [0] * (n2 + 1)

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[j] = 1 + dpPrev[j - 1]
            else:
                dp[j] = max(dp[j - 1], dpPrev[j])
        dpPrev = dp[:]

    return dp[n2]
  
print(maxUncrossedLines(nums1, nums2))

        
