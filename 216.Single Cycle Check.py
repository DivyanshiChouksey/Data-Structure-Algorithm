# Single Cycle Check
"""
    Here we start by keeping the record of number of visited elements 
    if we reached to the starting node without visiting all the nodes 
    thats means we have more than one cycle and return False
    or if after visiting all nodes and the current node is the starting node then we have only one cycle
    Note : cause array have negative values also so for the next idx mod the value by given array length 
"""

# Time Complexity = O(n) || Space Complexity = O(1)

array = [2, 3, 1, -4, -4, 2]


def hasSingleCycle(array):
    visited = 0
    i = 0
    while visited < len(array):
        if visited > 0 and i == 0:
            return False
        visited += 1
        i = getNextIdx(i, array)
    return i == 0


def getNextIdx(i, array):
    jump = array[i]
    nextIdx = (i + jump) % len(array)
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)


print(hasSingleCycle(array))
