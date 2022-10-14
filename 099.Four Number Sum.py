# Four Number Sum
array = [7, 6, 4, -1, 1, 2]
targetSum = 16


def fourNumberSum(array, targetSum):
    dct = {}
    tmp = []
    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in dct:
                for d in dct[difference]:
                    tmp.append(d + [array[i], array[j]])

        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum not in dct:
                dct[currentSum] = [[array[k], array[i]]]
            else:
                dct[currentSum].append([array[k], array[i]])
    return tmp


print(fourNumberSum(array, targetSum))
