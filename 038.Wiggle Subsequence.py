nums = [7,7,4,9,2,5]

count  = 2
preDiff = nums[1] - nums[0]
if preDiff==0:
    count = 1
for i in range(2,len(nums)):
    diff = nums[i] - nums[i-1]
    if preDiff >= 0 and diff < 0:
        count += 1
        preDiff = diff
    elif preDiff <= 0 and diff > 0:
        count += 1
        preDiff = diff
print(count)
