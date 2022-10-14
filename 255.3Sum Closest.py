#

nums = [-1, 2, 1, -4]
target = 1


def threeSumClosest(nums, target) -> int:
    nums.sort()
    res = sum(nums[:3])
    # ensure diff as a postive integer, so don't need use abs().
    diff = target - res if target > res else res - target

    for i in range(len(nums) - 2):

        if i > 0 and nums[i] == nums[i - 1]:
            # skip adjadcent duplicates
            continue

        l, r = i + 1, len(nums) - 1
        if nums[i] + nums[r - 1] + nums[r] <= target:
            # compare with the largest subset

            s = nums[i] + nums[r - 1] + nums[r]
            if s == target:
                return s

            if target - s < diff:
                res = s
                diff = target - s

        elif nums[i] + nums[l] + nums[l + 1] >= target:
            # compare with the smallest subset

            s = nums[i] + nums[l] + nums[l + 1]
            if s == target:
                return s

            if s - target < diff:
                res = s
                diff = s - target
        else:
            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s == target:
                    return s
                elif s < target:
                    l += 1
                    if target - s < diff:
                        res = s
                        diff = target - s
                else:
                    r -= 1
                    if s - target < diff:
                        res = s
                        diff = s - target
    return res
