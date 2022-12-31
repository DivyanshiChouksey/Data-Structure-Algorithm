# Single-Threaded CPU

# Time Complexity = O(nlogn) || Space Complexity = O(n)

import heapq

tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]


def getOrder(tasks):
    for i in range(len(tasks)):
        tasks[i].append(i)
    heap = []
    ans = []
    tasks.sort()
    curTime = tasks[0][0]
    for i in range(len(tasks)):
        while heap and curTime < tasks[i][0]:
            timeTaken, heapIndex = heapq.heappop(heap)
            ans.append(heapIndex)
            curTime += timeTaken
        if not heap and curTime < tasks[i][0]:
            curTime = tasks[i][0]
        heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
    while heap:
        timeTaken, heapIndex = heapq.heappop(heap)
        ans.append(heapIndex)
    # print(heap)
    return ans


print(getOrder(tasks))
