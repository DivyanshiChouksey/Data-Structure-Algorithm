# Minimum Waiting Time
"""
    Greedy Approach 
    The idea behind this is we need to figure out that executing shortest queries first is all
    will lead to the minimum Waiting Time becuase all the queries after it,
    again will wait minimum amount of time before they're executing (Sorting).
"""
# Time Complexity = O(nlogn) || Space Complexity = O(1)

queries = [6, 1, 3, 2, 2]


def minimumWaitingTime(queries):
    queries.sort()
    totalTime = 0
    for idx, duration in enumerate(queries):
        queriesLeft = len(queries) - (idx + 1)
        totalTime += duration * queriesLeft

    return totalTime


print(minimumWaitingTime(queries))
