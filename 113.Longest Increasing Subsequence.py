# Longest Increasing Subsequence

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
nums = [10, 9, 2, 5, 3, 7, 101, 18]


def lengthOfLIS(nums):
    seq = [1 for _ in nums]

    for i in range(len(nums)):
        for j in reversed(range(i)):  # 2,1,0
            if nums[j] < nums[i]:
                seq[i] = max(seq[i], seq[j] + 1)

    return max(seq)


print(lengthOfLIS(nums))
