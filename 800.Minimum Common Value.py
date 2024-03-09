# Minimum Common Value

nums1 = [12,16,24,24,25,27,31,37,38,41,43,50,57,70,71,71,74,76,77,78]
nums2 = [5,5,9,11,12,17,20,34,36,51,61,68,70,79,85,87,88,90,91,97]

def getCommon(nums1, nums2):
    i = 0
    j = 0
    while i<len(nums1) and j<len(nums2):
        if nums1[i] == nums2[j]:
            return nums1[i]
        elif nums1[i]<nums2[j]:
            i+=1
        else:
            j+=1
    return -1



print(getCommon(nums1, nums2))
