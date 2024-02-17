# Furthest Building You Can Reach

from collections import heapq

heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1

def furthestBuilding(heights, bricks, ladders):
    arr = []
    for i in range(len(heights)-1):
        diff = heights[i+1]-heights[i]
        if diff>0:
            heappush(arr,diff)

        if len(arr)>ladders:
            #pop the smallest value then sub from bricks
            bricks -= heappop(arr)

        if bricks<0:
            return i

    return len(heights)-1

print(furthestBuilding(heights, bricks, ladders))
