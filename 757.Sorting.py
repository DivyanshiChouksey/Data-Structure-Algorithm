# bubble sorted
array = [7, 1, 4, 6, 7, 3, 8, 9, 3, 2]
# def bubbleSort(array):
isSorted = False
counter = 0
while not isSorted:
    isSorted = True
    for i in range(len(array) - 1 - counter):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            isSorted = False
    counter += 1
print(array)


# merge Sort

array = [8, 5, 2, 9, 5, 6, 3]


def mergeSort(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2
    leftArray = array[:mid]
    rightArray = array[mid:]
    return mergeSortedArray(mergeSort(leftArray), mergeSort(rightArray))


def mergeSortedArray(arrayOne, arrayTwo):
    i, j = 0, 0
    out = []
    while i < len(arrayOne) and j < len(arrayTwo):
        if arrayOne[i] < arrayTwo[j]:
            out.append(arrayOne[i])
            i += 1
        else:
            out.append(arrayTwo[j])
            j += 1
    while i < len(arrayOne):
        out.append(arrayOne[i])
        i += 1
    while j < len(arrayTwo):
        out.append(arrayTwo[j])
        j += 1
    return out


print(mergeSort(array))
