# Maximum Element After Decreasing and Rearranging

arr = [2,2,1,2,1]

def maximumElementAfterDecrementingAndRearranging(arr):
    n = len(arr)
    counts = [0] * (n + 1)
    
    for num in arr:
        counts[min(num, n)] += 1
    
    ans = 1
    for num in range(2, n + 1):
        ans = min(ans + counts[num], num)

    return ans

print(maximumElementAfterDecrementingAndRearranging(arr))
