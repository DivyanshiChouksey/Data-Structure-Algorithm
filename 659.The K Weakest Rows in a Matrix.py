# The K Weakest Rows in a Matrix

import heapq

mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3

def kWeakestRows(mat,k):
    heap = []
    for i in range(len(mat)):
        tmp = 0
        for j in range(len(mat[i])):
            if mat[i][j] ==1:
                tmp+=1
        heapq.heappush(heap,(tmp,i))
    
    ans = []
    for i in range(k):
        ans.append(heapq.heappop(heap)[1])
    
    return ans 


print(kWeakestRows(mat,k))
