# Minimum Replacements to Sort the Array

nums = [3,9,3]

def minimumReplacement(nums):
    answer = 0
    n = len(nums)

    # Start from the second last element, as the last one is always sorted.
    for i in range(n - 2, -1, -1):
        # No need to break if they are already in order.
        if nums[i] <= nums[i + 1]:
            continue
        
        # Count how many elements are made from breaking nums[i].
        num_elements = (nums[i] + nums[i + 1] - 1) // nums[i + 1]
        
        # It requires numElements - 1 replacement operations.
        answer += num_elements - 1

        # Maximize nums[i] after replacement.
        nums[i] = nums[i] // num_elements

    return answer

print(minimumReplacement(nums))
