# Make Array Strictly Increasing

arr1 = [1,5,3,6,7]
arr2 = [1,3,2,4]


def makeArrayIncreasing(arr1, arr2):
    dp = {-1: 0}
    arr2.sort()
    n = len(arr2)

    for i in range(len(arr1)):
        new_dp = collections.defaultdict(lambda: float('inf'))
        for prev in dp:
            if arr1[i] > prev:
                new_dp[arr1[i]] = min(new_dp[arr1[i]], dp[prev])
            idx = bisect.bisect_right(arr2, prev)
            if idx < n:
                new_dp[arr2[idx]] = min(new_dp[arr2[idx]], 1 + dp[prev])
        dp = new_dp

    return min(dp.values()) if dp else -1
  
print(makeArrayIncreasing(arr1, arr2))
