# Can Place Flowers
"""
    in this we'll try to find 3 contiguous empty spots
    for some edge cases we assume one empty spots befor beginning and
    one after the end
"""
# Time Complexity = O(n) || Space Complexity = O(1)

flowerbed = [1,0,0,0,1]
n = 1

def canPlaceFlower(flowerbed,n):
    f = [0]+ flowerbed +[0]
    for i in range(1,len(f)-1):
        if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
            f[i] = 1
            n -= 1
    return n <= 0

print(canPlaceFlower(flowerbed,n))