# Next Greater Element I

nums1 = [4,1,2]
nums2 = [1,3,4,2]

dct = {}
for i in range(len(nums2)):
    for j in range (i,len(nums2)):
        if nums2[j] > nums2[i]:
            dct[nums2[i]] = nums2[j]
            break
        if j == len(nums2)-1:
            dct[nums2[i]] = -1
            
ans = []
for i in range(len(nums1)):
    ans.append(dct[nums1[i]])
print(ans)






# Naive Solution
ans = []
for i in range(len(nums1)):
    for j in range (len(nums2)):
        if nums1[i] == nums2[j]:
            for k in range(j,len(nums2)):
                if nums2[k] > nums2[j]:
                    ans.append(nums2[k])
                    break
                if k==len(nums2)-1:
                    ans.append(-1)
            # k = j+1

            # while k<len(nums2) and nums2[j] > nums2[k] :     #4<2
            #     k += 1
            # if k==len(nums2):
            #     ans.append(-1)
            # else:
            #     ans.append(nums2[k])

print(ans)