# The Skyline problem

# Time Complexity = O(nlogn) || Space Complexity = O(n)

from heapq import heappop, heappush


buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
# add start-building events
# also add end-building events(acts as buildings with 0 height)
# and sort the events in left -> right order
events = [(L, -H, R) for L, R, H in buildings]
events += list({(R, 0, 0) for _, R, _ in buildings})
events.sort()
print(events)
# res: result, [x, height]
# live: heap, [-height, ending position]
res = [[0, 0]]
current = [(0, float("inf"))]  # heap

for pos, negH, R in events:
    # 1, pop buildings that are already ended
    # 2, if it's the start-building event, make the building current
    # 3, if previous keypoint height != current highest height, edit the result

    while current[0][1] <= pos:  # ending position<=current pos
        heappop(current)
    if negH != 0:
        heappush(current, (negH, R))
    if res[-1][1] != -current[0][0]:
        res += [[pos, -current[0][0]]]

print(res[1:])
