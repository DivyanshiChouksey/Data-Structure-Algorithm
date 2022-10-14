# Sum of Even Numbers After Queries

nums = [1, 2, 3, 4]
queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]


def sumEvenAfterQueries(nums, queries):
    res = []
    ans = 0
    for n in nums:
        if n % 2 == 0:
            ans += n

    for k, v in queries:
        if nums[v] % 2 == 0:
            ans -= nums[v]
        nums[v] += k
        if nums[v] % 2 == 0:
            ans += nums[v]
        res.append(ans)
    return res


print(sumEvenAfterQueries(nums, queries))
