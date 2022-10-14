# Maximize Expression

array = [3, 6, 1, -3, 2, 7]


def maximizeExpression(array):
    if len(array) < 4:
        return 0

    maxValue = float("-inf")

    for a in range(len(array)):
        for b in range(a + 1, len(array)):
            for c in range(b + 1, len(array)):
                for d in range(c + 1, len(array)):
                    expression = array[a] - array[b] + array[c] - array[d]
                    maxValue = max(maxValue, expression)

    return maxValue


def maximizeExpression2(array):
    if len(array) < 4:
        return 0

    maxOfA = [array[0]]
    maxOfAMinusB = [float("-inf")]
    maxOfAMinusBPlusC = [float("-inf")] * 2
    maxOfAMinusBPlusCMinusD = [float("-inf")] * 3

    for i in range(1, len(array)):
        current = max(maxOfA[i - 1], array[i])
        maxOfA.append(current)

    for i in range(1, len(array)):
        current = max(maxOfAMinusB[i - 1], maxOfA[i - 1] - array[i])
        maxOfAMinusB.append(current)

    for i in range(2, len(array)):
        current = max(maxOfAMinusBPlusC[i - 1], maxOfAMinusB[i - 1] + array[i])
        maxOfAMinusBPlusC.append(current)

    for i in range(3, len(array)):
        current = max(
            maxOfAMinusBPlusCMinusD[i - 1], maxOfAMinusBPlusC[i - 1] - array[i]
        )
        maxOfAMinusBPlusCMinusD.append(current)

    return maxOfAMinusBPlusCMinusD[-1]


print(maximizeExpression(array))
print(maximizeExpression2(array))
