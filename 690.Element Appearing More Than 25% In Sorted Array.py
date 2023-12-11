# Element Appearing More Than 25% In Sorted Array

arr = [1,2,2,6,6,6,6,7,10]


def findSpecialInteger(arr):
    counts = defaultdict(int)
    for num in arr:
        counts[num] += 1
        
    target = len(arr) / 4
    for key, value in counts.items():
        if value > target:
            return key
        
    return -1


print(findSpecialInteger(arr))
