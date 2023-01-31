# Next Greater Element II

# Naive Solution
"""
    Using two for loops and to move in a circular way update nums as nums+nums after that
    update the next greater value of current element in ans array and return ans.

"""
# Time Complexity = O(n^2) || Space Complexity = O(n)

nums = [1,2,3,4,3]   # output = [2,3,4,-1,4]

def nextGreaterElements1(nums):
    ans = [-1]*len(nums)
    nums = nums+nums
    for i in range(len(nums)//2):
        for j in range(i,len(nums)):
            if nums[i] < nums[j]:
                ans[i] = nums[j]
                break
    return ans


# Optimized Solution
"""
    This approach makes use of a stack. This stack stores the appropriate elements from nums array. 
    The top of the stack refers of the Next Greater Element found so far, and an result array of len(nums).
    Traversing the nums array from right towards the left twise and pop all element 
    if stack[top]<= current element and if not that means stack[top] is the next greater element for that current 
    value so update result[i] with stack[top] value else just push the element in stack 
    at the end return result.

"""
# Time Complexity = O(n) || Space Complexity = O(n)

nums = [1,2,3,4,3]    # output = [2,3,4,-1,4]

def nextGreaterElements2(nums):
    res = [-1]*len(nums)
    stack = []
    for i in range(2):
        for i in reversed(range(len(nums))):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack and res[i]==-1:
                res[i] = stack[-1]
            stack.append(nums[i])
    return res



print(nextGreaterElements1(nums))
print(nextGreaterElements2(nums))
