# Longest Subsequence With Limited Sum

nums = [4, 5, 2, 1]
queries = [3, 10, 21]


def answerQueries(nums, queries):
    nums.sort()
    result = []
    for q in queries:
        curr = idx = 0
        tmp = q
        while idx < len(nums):
            if curr + nums[idx] > tmp:
                break
            curr += nums[idx]
            idx += 1
        result.append(idx)

    return result
