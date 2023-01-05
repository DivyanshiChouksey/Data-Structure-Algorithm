# Minimum Number of Arrows to Burst Balloons

"""
    As we know overlapping cordinates of balloons will need only an arrow to burst all of them
    so just go through the sorted points array and keep track of previous ending cordinate of balloon 
    if current starting cordinate is greater then prev means no overlapping then increase count of arrows and 
    return arrow.
"""

# Time Complexity = O(nlogn) || Space Complexity = O(1)

points = [[10, 16], [2, 8], [1, 6], [7, 12]]


def findMinArrowShots(points):
    points.sort(key=lambda x: x[1])
    arrows = 1
    prev = points[0][1]
    # print(prev)
    for i in range(1, len(points)):
        curStart, curEnd = points[i]
        # print(curStart,curEnd)
        if curStart > prev:
            prev = curEnd
            arrows += 1
    return arrows


print(findMinArrowShots(points))
