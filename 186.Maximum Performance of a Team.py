# Maximum Performance of a Team

n = 6
speed = [2, 10, 3, 1, 5, 8]
efficiency = [5, 4, 3, 9, 7, 2]
k = 2


import heapq


def maxPerformance(n, speed, efficiency, k):
    engineers = [engineer for engineer in zip(efficiency, speed)]
    # * Sort in descending order based on the efficiency.
    engineers.sort(key=lambda engineer: -engineer[0])
    min_heap = []
    max_performance = total_speed = 0
    for cur_efficiency, cur_speed in engineers:
        if len(min_heap) == k:
            total_speed -= heapq.heappop(min_heap)
        total_speed += cur_speed
        heapq.heappush(min_heap, cur_speed)
        max_performance = max(max_performance, cur_efficiency * total_speed)

    return max_performance % (10**9 + 7)


print(maxPerformance(n, speed, efficiency, k))
