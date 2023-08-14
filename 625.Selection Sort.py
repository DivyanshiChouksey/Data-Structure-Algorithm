# Selection Sort

"""
  Best Time : O(n^2)  || Space : O(1)
  Average Time : O(n^2)  || Space : O(1)
  Worst Time : O(n^2)  || Space : O(1)
"""
array = [8, 5, 2, 9, 5, 6, 3]

def selectionSort(array):
    cur = 0
    while cur < len(array)-1:
        small = cur
        for i in range(cur+1, len(array)):
            if array[small] > array[i] :
                small = i
        array[cur] , array[small] = array[small] , array[cur]
        cur+=1
        
    return array


print(selectionSort(array))
