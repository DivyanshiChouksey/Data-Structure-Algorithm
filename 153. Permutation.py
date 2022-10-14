arr = [1, 2, 3]
permutations = []


def helper(arr, current, permutations):
    if len(arr) == 0 and len(current) != 0:
        permutations.append(current)
    else:
        for i in range(len(arr)):
            newArr = arr[:i] + arr[i + 1 :]
            newPer = current + [arr[i]]
            helper(newArr, newPer, permutations)


helper(arr, [], permutations)
print(permutations)
