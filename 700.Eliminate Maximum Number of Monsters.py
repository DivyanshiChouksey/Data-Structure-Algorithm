# Eliminate Maximum Number of Monsters

dist = [3,2,4], speed = [5,3,2]

import heapq

def eliminateMaximum(dist, speed):

    heap = []
    for i in range(len(dist)):
        heap.append(dist[i] / speed[i])
        
    heapq.heapify(heap)
    ans = 0
    while heap:
        if heapq.heappop(heap) <= ans:
            break
        ans += 1
    return ans


print(eliminateMaximum(dist, speed))

def eliminateMaximum(dist, speed):
    arrival = []
    for i in range(len(dist)):
        arrival.append(dist[i]/speed[i])

    arrival.sort()
    ans = 0

    for i in range(len(arrival)):
        if arrival[i] <= i:
            break
        ans+=1
    return ans

print(eliminateMaximum(dist, speed))
