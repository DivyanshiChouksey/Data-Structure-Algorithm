# Arithmetic Subarrays

nums = [4,6,5,9,3,7]
l = [0,0,2]
r = [2,3,5]


def checkArithmeticSubarrays(nums, l, r):
    def check(arr):
        min_element = min(arr)
        max_element = max(arr)

        if (max_element - min_element) % (len(arr) - 1) != 0:
            return False

        diff = (max_element - min_element) / (len(arr) - 1)
        
        arr_set = set(arr)
        curr = min_element + diff
        while curr < max_element:
            if curr not in arr_set:
                return False
            
            curr += diff
        
        return True

    ans = []
    for i in range(len(l)):
        arr = nums[l[i] : r[i] + 1]
        ans.append(check(arr))
    
    return ans


print(checkArithmeticSubarrays(nums, l, r))
