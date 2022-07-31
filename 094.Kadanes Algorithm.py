# Kadanes Algorithm (Maximum Subarray)
"""
    array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
    maxEnd = 3  8  -1  1  4   2  5  9 16  18  9  15 18 19  14 10
    maxSoFar 3  8   8  8  8   8  8  9 16  18 18  18 18 19  19 19
    
    We can create a hashmap of the greatest sum for the subarray ending at the index(0,1,2,...)
    we can either sum-up using the number of that index or we can go for only the number of that index 
    that means we are trying to find maximum sum ending at that index  ,
    and as well as keep the track of the maximum value we found so far and at the end return the maximum so far


"""
array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]


def kadanesAlgorithm(array):
    maxEnding = array[0]
    maxSoFar = array[0]
    for i in range(1, len(array)):
        maxEnding = max(array[i], maxEnding + array[i])
        maxSoFar = max(maxSoFar, maxEnding)
    return maxSoFar


print(kadanesAlgorithm(array))
