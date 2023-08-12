# Merge Sort

"""
    best : O(nlogn) time || Space : O(nlogn)
    average : O(nlogn) time || Space : O(nlogn)
    worst : O(nlogn) time || Space : O(nlogn)
"""

array = [8, 5, 2, 9, 5, 6, 3]

def mergeSort(array):
    if len(array)==1:
        return array
    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]
    return helper(mergeSort(left),mergeSort(right))

def helper(left,right):
    sortedArray = [None]*(len(left)+len(right))
    k=i=j=0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            sortedArray[k] = left[i]
            i+=1
        else:
            sortedArray[k] = right[j]
            j+=1
        k+=1
    while i<len(left):
        sortedArray[k] = left[i]
        i+=1
        k+=1
    while j<len(right):
        sortedArray[k] = right[j]
        j+=1
        k+=1

    return sortedArray
        
            

print(mergeSort(array))