# Validate Sequence

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

# Solution 1
# Time Complexity = O(n) || Space Complexity = O(1)
def isValidSubsequence(array, sequence):
    i = 0
    j = 0
    while i < len(array) and j < len(sequence):
        if array[i] == sequence[j]:
            j += 1
        i += 1
    return j == len(sequence)


# Solution 2
# Time Complexity = O(n) || Space Complexity = O(1)
def isValidSubsequence2(array, sequence):
    i = 0
    for value in array:
        if i == len(sequence):
            break
        if sequence[i] == value:
            i += 1
    return i == len(sequence)


print(isValidSubsequence(array, sequence))
print(isValidSubsequence2(array, sequence))
