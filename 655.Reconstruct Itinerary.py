# Reconstruct Itinerary
from collections import defaultdict 

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

def findItinerary(tickets):
    dct = defaultdict(list)
    for a,b in sorted(tickets)[::-1]:
        dct[a].append(b)

    route = []
    def dfs(node):
        while dct[node]:
            dfs(dct[node].pop())
        route.append(node)

    dfs("JFK")
    return route[::-1]

print(findItinerary(tickets))
