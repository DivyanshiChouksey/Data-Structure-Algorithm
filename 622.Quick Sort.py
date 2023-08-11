# Quick Sort

"""
    best : O(nlogn) time || Space : O(logn)
    average : O(nlogn) time || Space : O(logn)
    worst : O(n^2) time || Space : O(logn)
"""

array = [8, 5, 2, 9, 5, 6, 3]

def quickSort(array):
    helper(array,0,len(array)-1)
    return array

def helper(array,start,end):
    if start>=end:
        return 
    pivot = start
    l = start+1
    r = end
    while r >= l:
        if array[l] > array[pivot] and array[r] <array[pivot]:
            array[l],array[r] = array[r],array[l]
        if array[l] <= array[pivot]:
            l+=1
        if array[r] >= array[pivot]:
            r-=1

    array[pivot], array[r] = array[r],array[pivot]
    isLeftsmaller  = r-start-1 < end -(r+1)
    if isLeftsmaller:
        helper(array,start,r-1)
        helper(array,r+1,end)
    else:
        helper(array ,r+1,end)
        helper(array,start,r-1)
        
    
print(quickSort(array))