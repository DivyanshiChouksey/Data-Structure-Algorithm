# Search a 2D Matrix


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3


def searchMatrix(matrix, target):
    r1 = 0
    r2 = len(matrix)-1
    c1 = 0
    c2 = len(matrix[0])-1

    while r1<=r2:
        mid = (r1+r2)//2
        if matrix[mid][0] == target:
            return True
        if matrix[mid][0] >= target:
            r2 = mid-1
        else:
            r1 = mid+1
        
    while c1<=c2:
        mid = (c1+c2)//2
        if matrix[r2][mid] == target:
            return True
        if matrix[r2][mid] >= target:
            c2 = mid-1
        else:
            c1 = mid+1
        
    return False

print(searchMatrix(matrix, target))
