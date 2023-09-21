# Median of Two Sorted Arrays

nums1 = [1,2]
nums2 = [3,4]

def findMedianSortedArrays(nums1,nums2):
    merged = []
    i, j = 0, 0
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
            
    while i < len(nums1):
        merged.append(nums1[i])
        i += 1
        
    while j < len(nums2):
        merged.append(nums2[j])
        j += 1
    
    mid = len(merged) // 2
    if len(merged) % 2 == 0:
        return (merged[mid-1] + merged[mid]) / 2
    else:
        return merged[mid]


print(findMedianSortedArrays(nums1,nums2))
