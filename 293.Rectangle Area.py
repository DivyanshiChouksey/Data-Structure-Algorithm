# Rectangle Area

"""
    Find the area of both rectangle separately then find the area of overlapping rectangle 
    then add both area of rectangle subtract overlapping area to get desire output
    so for overlapping find the leftmost point of intersection rectangle that is  max(ax1, bx1)
    rightmost point of intersection rectangle that is min(ax2, bx2) and similarly 
    topmost point that is min(ay2, by2) and bottom-most point that is max(ay1, by1).

"""

# Time Complexity = O(1) || Space Complexity = O(1)

ax1 = -3
ay1 = 0
ax2 = 3
ay2 = 4
bx1 = 0
by1 = -1
bx2 = 9
by2 = 2


def computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    totalArea = 0
    areaOfOverlap = 0

    rl1 = ax2 - ax1
    rb1 = ay2 - ay1
    areaOfA = rl1 * rb1

    rl2 = bx2 - bx1
    rb2 = by2 - by1
    areaOfB = rl2 * rb2

    left = max(ax1, bx1)  # leftmost point of intersection rectangle
    right = min(ax2, bx2)
    overlapOfX = right - left

    bottom = max(ay1, by1)  # leftmost point of intersection rectangle
    top = min(ay2, by2)
    overlapOfY = top - bottom
    if overlapOfY > 0 and overlapOfX > 0:
        areaOfOverlap = overlapOfX * overlapOfY
    total = areaOfA + areaOfB - areaOfOverlap
    return total


print(computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2))
