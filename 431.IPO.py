# IPO

import heapq

k = 3
w = 0
profits = [1,2,3,1]
capital = [0,1,1,2]

def findMaximizedCapital(k, w, profits, capital):
    projects = list(zip(capital,profits))
    projects.sort()
    heap = []
    i = 0
    for _ in range(k):
        while i<len(projects) and projects[i][0]<=w:
            heapq.heappush(heap,-projects[i][1])
            i+=1
        if heap:
            w-=(heapq.heappop(heap))

    return w

print(findMaximizedCapital(k, w, profits, capital))