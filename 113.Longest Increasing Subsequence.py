# Longest Increasing Subsequence

nums = [10, 9, 2, 5, 3, 7, 101, 18]

# Naive Solution
"""
    nums = [10, 9, 2, 5, 3, 7, 101, 18] 
    idx      0  1  2  3  4  5   6    7
    At idx = 3
    seq =   [1, 1, 1, 2, 2, 3,  4,   4]

    Let's assume that every element in array is a subsequence so for this creating a sequence array to keep track of largest sequence
    go through the array in reverse order from the current element and check for smaller values than current value
    then update sequence of current value with the maximum of sequence value and current sequence (seq[i] = max(seq[i], seq[j] + 1))

"""
# Time Complexity = O(n^2) || Space Complexity = O(n)


def lengthOfLIS(nums):
    seq = [1 for _ in nums]
    for i in range(len(nums)):
        for j in reversed(range(i)):  # 2,1,0
            if nums[j] < nums[i]:
                seq[i] = max(seq[i], seq[j] + 1)
    return max(seq)


# Optimized Solution
"""
    Initialize an empty array name as sequence
    go through the array nums and find out the position of that element in sequence array (ie. find the index of the element in sequence array)
    if len(seq) == index of that element then append the element in our sequence array,
    else update that index value with this element 
    and return length of sequence
"""
# Time Complexity = O(nlogn) || Space Complexity = O(n)


def lengthOfLIS2(nums):
    seq = []

    def binarySearch(num, seq):
        l = 0
        r = len(seq)
        while l < r:
            mid = (l + r) // 2
            if seq[mid] < num:
                l = mid + 1
            else:
                r = mid
        return l

    for num in nums:
        idx = binarySearch(num, seq)
        if len(seq) == idx:
            seq.append(num)
        else:
            seq[idx] = num
    return len(seq)


# Solution 2
import bisect


def lengthOfLIS3(nums):
    seq = []
    for num in nums:
        idx = bisect.bisect_left(seq, num)
        if len(seq) == idx:
            seq.append(num)
        else:
            seq[idx] = num
    return len(seq)


print(lengthOfLIS(nums))
print(lengthOfLIS2(nums))
print(lengthOfLIS3(nums))
