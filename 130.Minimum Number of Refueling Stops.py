# Minimum Number of Refueling Stops

import heapq

target = 100
startFuel = 10
stations = [[10, 60], [20, 30], [30, 30], [60, 40]]


def minRefuelStops(target, startFuel, stations):

    pq = []  # A maxheap is simulated using negative values
    stations.append((target, float("inf")))

    ans = prev = 0
    for location, capacity in stations:
        startFuel -= location - prev
        while pq and startFuel < 0:  # must refuel in past
            startFuel += -heapq.heappop(pq)
            ans += 1
        if startFuel < 0:
            return -1
        heapq.heappush(pq, -capacity)
        prev = location

    return ans


print(minRefuelStops(target, startFuel, stations))
