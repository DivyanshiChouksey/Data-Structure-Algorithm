# Insert Interval

intervals = [[1, 2], [3, 8], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]

"""
    Naïve approach - directly append the newInterval in our intervals array then sort it and perform merge overlapping interval.
    it will take - O(nlog(n)) Time

    Optimization we are given it in sorted order so we can do this in linear time just by clever understanding of question
    First find the place of insertion then check the merging intervals steps to do above approach -

    1. Go through the intervals array and to insert newInterval once keep track of interval so check
       if current end is smaller than newInterval start then append the current interval in our ans array.
    2. If current start is greater than newInterval and the newInterval is not inserted yet then append
       the newInterval in our ans and marked inserted
    3. If the values are overlapping then, update newInterval start with min of newInterval start and
       current start, and newInterval end with max of newInterval end and current end.
       
    NOTE :- the edge case after the iteration if not newInterval is not inserted yet then
    at last append it to the ans. (do this with help of flag)
"""

# Time Complexity = O(n) || Space Complexity = O(n)


def insert(intervals, newInterval):
    inserted = False
    ans = []
    for interval in intervals:
        if interval[1] < newInterval[0]:
            ans.append(interval)
        elif interval[0] > newInterval[1]:
            if not inserted:
                ans.append(newInterval)
                inserted = True
            # merge here 1 time
            ans.append(interval)
        else:
            newInterval[0] = min(newInterval[0], interval[0])
            newInterval[1] = max(newInterval[1], interval[1])

    if not inserted:
        ans.append(newInterval)
    return ans


print(insert(intervals, newInterval))
