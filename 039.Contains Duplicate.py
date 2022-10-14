# Contain Duplicate

nums = [1,2,3,1]

seen = set()
for num in nums:
    if num in seen:
        print("True")
    seen.add(num)
print("False")


# solution 2
nums.sort()
for i in range(1,len(nums)):
    if nums[i] == nums[i-1]:
        print("True")
print("False")

# sol 3
seen = {}
for num in nums:
    if num in seen:
        print("True")
    seen[num] = True
print("False")
