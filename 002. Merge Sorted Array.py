# Merge Sorted Array

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# Naive Solution
"""
    take another empty list 
    append value in sorted manner then update nums1 as list 
"""
# Time Complexity = O(n+m) || Space Complexity = O(n+m)
def merge(nums1, m, nums2, n):
    i = 0
    j = 0
    nums3 = []
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            nums3.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            nums3.append(nums2[j])
            j += 1
        elif nums1[i] == nums2[j]:
            nums3.append(nums1[i])
            i += 1
            nums3.append(nums2[j])
            j += 1

    while i < m:
        nums3.append(nums1[i])
        i += 1

    while j < n:
        nums3.append(nums2[j])
        j += 1

    i = 0
    nums1[i:] = nums3[i:]
    return nums1



# Optimized Solution
"""
    we need to change all values in our nums1 
    so we start by taking 2 pointers from the end and
    then compare the largest value then update it from back(reverse) in nums1
    After that check for remaining elements in nums2
"""
# Time Complexity = O(n+m) || Space Complexity = O(1)
def merge2(nums1, m, nums2, n):
    last = m+n-1
    while m > 0 and n > 0 :
        if nums1[m-1] > nums2[n-1]:
            nums1[last] = nums1[m-1]
            m -= 1
        else:
            nums1[last] = nums2[n-1]
            n -= 1
        last -= 1

    while n > 0:
        nums1[last] = nums2[n-1]
        n -= 1
        last -= 1
  


print(merge(nums1, m, nums2, n))
print(nums1)


