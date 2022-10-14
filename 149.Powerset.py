# Powerset
array = [1, 2, 3]


def powerset(array):
    subsets = [[]]
    for ele in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [ele])
    return subsets


def powerset1(array, idx):
    if idx is None:
        idx = len(array) - 1
    if idx < 0:
        return [[]]
    ele = array[idx]
    subsets = powerset1(array, idx - 1)
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [ele])
    return subsets


print(powerset(array))
print(powerset1(array, None))
