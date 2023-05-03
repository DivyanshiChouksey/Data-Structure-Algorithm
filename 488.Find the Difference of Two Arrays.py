# Find the Difference of Two Arrays

nums1 = [1,2,3]
nums2 = [2,4,6]

def findDifference1(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    tmp=[]
    for n in set1:
        if n not in set2:
            tmp.append(n)

    tmp2 = []
    for i in set2:
        if i not in set1:
            tmp2.append(i)

    return [tmp,tmp2]
  
def findDifference2(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return [list(set1.difference(set2)), list(set2.difference(set1))]


print( findDifference1(nums1, nums2))
print( findDifference2(nums1, nums2))
