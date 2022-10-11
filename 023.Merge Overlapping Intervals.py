# Merge Overlapping intervals

# Time Complexity = O(nlogn) || Space Complexity = O(n)

intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]


def mergeOverlappingIntervals(intervals):
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    currentInterval = sortedIntervals[0]
    out = []
    out.append(currentInterval)
    for interval in sortedIntervals:
        currentStart, currentEnd = currentInterval
        nextStart, nextEnd = interval
        if currentEnd >= nextStart:
            currentInterval[1] = max(currentEnd, nextEnd)
        else:
            currentInterval = interval
            out.append(currentInterval)
    return out


print(mergeOverlappingIntervals(intervals))
