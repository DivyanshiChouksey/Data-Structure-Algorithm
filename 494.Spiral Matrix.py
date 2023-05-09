# Spiral Matrix

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

def spiralOrder(matrix):
    t = 0
    b = len(matrix)-1
    i = 0
    j = len(matrix[0])-1

    ans = []

    while i<=j and t<=b:
        for x in range(i,j+1):
            ans.append(matrix[t][x])
        for x in range(t+1,b+1):
            ans.append(matrix[x][j])
        for x in range(j-1,i-1,-1):
            if t == b:
                break
            ans.append(matrix[b][x])
        for x in range(b-1,t,-1):
            if i==j:
                break
            ans.append(matrix[x][i])

        i+=1
        t+=1
        b-=1
        j-=1

    return ans
  
print(spiralOrder(matrix))
