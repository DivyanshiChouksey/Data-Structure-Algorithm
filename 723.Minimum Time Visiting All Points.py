# Minimum Time Visiting All Points

points = [[1,1],[3,4],[-1,0]]


def minTimeToVisitAllPoints(points):
    time = 0
    for i in range(len(points)-1):
        x = points[i][0] - points[i+1][0]
        y = points[i][1] - points[i+1][1]
        time+= max(abs(x),abs(y))
    return time


print( minTimeToVisitAllPoints(points))
