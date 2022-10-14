# Longest Consecutive Sequence

nums = [100, 4, 200, 1, 3, 2]


def longestConsecutive(nums) -> int:
    count = 0
    nums = set(nums)
    for num in nums:
        if num - 1 not in nums:
            tmpCnt = 0
            while num in nums:
                num += 1
                tmpCnt += 1
            count = max(count, tmpCnt)
    return count


print(longestConsecutive(nums))
