# Max Dot Product of Two Subsequences


nums1 = [2,1,-2,5]
nums2 = [3,0,-6]


def maxDotProduct(nums, nums2):
    if max(nums1) < 0 and min(nums2) > 0:
        return max(nums1) * min(nums2)
    
    if min(nums1) > 0 and max(nums2) < 0:
        return min(nums1) * max(nums2)
    
    dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
    for i in range(len(nums1) - 1, -1, -1):
        for j in range(len(nums2) - 1, -1, -1):
            use = nums1[i] * nums2[j] + dp[i + 1][j + 1]
            dp[i][j] = max(use, dp[i + 1][j], dp[i][j + 1])
    
    return dp[0][0]

print( maxDotProduct(nums, nums2))
