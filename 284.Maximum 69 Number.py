# Maximum 69 Number

"""
    Replace first 6 into 9 to make the num largest
"""

# Time Complexity = O(n) || Space Complexity = O(n)

num = 9669


def maximum69Number(num):
    nums = list(str(num))
    for i in range(len(nums)):
        if nums[i] == "6":
            nums[i] = "9"
            break
    return int("".join(nums))


print(maximum69Number(num))
