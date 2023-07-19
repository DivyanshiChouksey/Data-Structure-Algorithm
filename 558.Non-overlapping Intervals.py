# Non-overlapping Intervals

intervals = [[1,2],[2,3],[3,4],[1,3]]


def eraseOverlapIntervals(intervals):
    intervals.sort(key = lambda x:x[1])
    count = 0
    psp = intervals[0][0]
    pep=intervals[0][1]
    for i in range(1,len(intervals)):
        if pep > intervals[i][0]:
            count+=1
        else:
            psp = intervals[i][0]
            pep = intervals[i][1]
    return count


print(eraseOverlapIntervals(intervals))
