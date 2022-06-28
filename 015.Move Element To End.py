# Move Element To End
"""
    take two pointers one at the beginning and another at the end and
    compare them to the value given to move if it is equal then swap otherwise continue
"""
# Time Complexity = O(n) || Space Complexity = O(1)

array = [2,4,2,5,6,2,2]
toMove = 2

def moveElementToEnd(array,toMove):
    i = 0
    j = len(array)-1
    while i < j:
        while i < j and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            array[i] , array[j] = array[j] , array[i]
        i += 1
    return array

print(moveElementToEnd(array,toMove))