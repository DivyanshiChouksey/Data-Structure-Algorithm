# Sum of Subarray Minimums

# arr = [11,81,94,43,3]
arr = [3, 1, 2, 4]


def sumSubarrayMins1(arr):
    ans = 0
    for i in range(len(arr)):
        tmp = arr[i]
        for j in range(i, len(arr)):
            tmp = min(tmp, arr[j])
            ans += tmp
    return ans


print(sumSubarrayMins1(arr))


def sumSubarrayMins2(arr):
    MOD = 10**9 + 7
    stack = []
    ans = 0

    for i in range(len(arr) + 1):
        while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
            mid = stack.pop()
            left_boundary = -1 if not stack else stack[-1]
            right_boundary = i

            # count of subarrays where mid is the minimum element
            count = (mid - left_boundary) * (right_boundary - mid)
            ans += count * arr[mid]

        stack.append(i)

    return ans % MOD


print(sumSubarrayMins2(arr))


def sumSubarrayMins(arr):
    ans = 0
    for i in range(len(arr)):
        tmp = arr[i]
        for j in range(i, len(arr)):
            tmp = min(tmp, arr[j])
            ans += tmp
    return ans


print(sumSubarrayMins(arr))
