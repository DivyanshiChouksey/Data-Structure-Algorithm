# Same BST


arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]

def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
        return False

    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True

    if arrayOne[0] != arrayTwo[0]:
        return False

    leftOne = getSmaller(arrayOne)
    leftTwo = getSmaller(arrayTwo)
    rightOne = getBigger(arrayOne)
    rightTwo = getBigger(arrayTwo)

    return sameBsts(leftOne,leftTwo) and sameBsts(rightOne,rightTwo)


def getSmaller(array):
    smaller = []
    for i in range(1,len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
    return smaller


def getBigger(array):
    bigger = []
    for i in range(1,len(array)):
        if array[i] >= array[0]:
            bigger.append(array[i])
    return bigger
