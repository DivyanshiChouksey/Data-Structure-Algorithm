nums1 = [0, 0, 0, 0, 1]
nums2 = [1, 0, 0, 0, 0]
i = 0
j = 0
maxcount = 0
while i < len(nums1):
    while j < len(nums2):
        count = 0
        while i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j]:
            count += 1
            i += 1
            j += 1
        maxcount = max(maxcount, count)
        j += 1
    i += 1
