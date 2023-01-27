# Cheapest Flights Within K Stops

"""
    We make an array dist of size n where we keep the track of min cost of reaching node
    from given source then we write a bfs which would stop early if we reach k steps 
    in that bfs we update the min cot of reaching that node and then in our provide 
    the total cost of reaching that node return dist[destination]
"""

# Time Complexity = o(n) || Space Complexity = O(n)

from collections import defaultdict

n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1


def findCheapestPrice(n, flights, src, dst, k):
    # single souce shortest path
    dist = [float("inf")] * n
    dct = defaultdict(list)
    for f, t, p in flights:
        dct[f].append([t, p])
    queue = [(src, 0)]
    stops = 0
    while queue and stops <= k:
        tmp = []
        for node, cur in queue:
            for child, cost in dct[node]:
                if cur + cost < dist[child]:
                    dist[child] = cur + cost
                    tmp.append(
                        (child, dist[child])
                    )  # we need total cost of reaching that element hence we are using dist[child]
        queue = tmp[:]
        stops += 1
    # print(dct)
    return dist[dst] if dist[dst] != float("inf") else -1


print(findCheapestPrice(n, flights, src, dst, k))
