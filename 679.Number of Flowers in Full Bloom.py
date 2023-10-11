# Number of Flowers in Full Bloom

from bisect import bisect_right, bisect_left

A = [[1,6],[3,7],[9,12],[4,13]]
poeple = [2,3,7,11]


def fullBloomFlowers(A, persons):
    start, end = sorted(a for a,b in A), sorted(b for a,b in A)
    return [bisect_right(start, t) - bisect_left(end, t) for t in persons]  

print(fullBloomFlowers(A, persons) 
