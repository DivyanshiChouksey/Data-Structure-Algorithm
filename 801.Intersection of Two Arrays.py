# Intersection of Two Arrays

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]


def intersection(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    ans = []
    for num in nums1:
        if num in nums2:
            ans.append(num)
    return ans

print(intersection(nums1, nums2))
