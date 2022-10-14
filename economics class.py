from itertools import combinations

# [Verfication of the code][1]
# function to generate all subsets possible, there will be 2^n - 1 subsets(combinations)
def subsets(arr):
    temp = []
    for i in range(1, len(arr) + 1):
        comb = combinations(arr, i)
        for j in comb:
            temp.append(j)
    return temp


# function to calculate median
def median(arr):
    mid = len(arr) // 2
    if len(arr) % 2 == 0:
        median = (arr[mid] + arr[mid - 1]) / 2
    else:
        median = arr[mid]
    return median


# function to calculate median
def mean(arr):
    temp = 0
    for i in arr:
        temp = temp + i
    return temp / len(arr)


# function to solve given problem
def meanMedian(arr):
    sets = subsets(arr)
    max_value = 0
    for i in sets:
        mean_median = mean(i) - median(i)
        if mean_median > max_value:
            max_value = mean_median
            needed_set = i
    return needed_set


arr = [1, 2, 3, 4]
print(meanMedian(arr))
