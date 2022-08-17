# Sunset Views
"""
    Here the approach is we iterate through the given array and keep record of maximum height
    if we found any value greater than our maximum height then append it to our ans thats mean the building can see sunset view,
    now our new maximum height will be the greater value and at last return ans 
    Note :- For "EAST" direction iterate in reversed order and also return ans in reversed sequence.

"""
# Time Complexity = O(n) || Space Complexity = O(n)
buildings = [1, 2, 3, 1, 5, 6, 9, 1, 9, 9, 11, 10, 9, 12, 8]
direction = "WEST"


def sunsetViews(buildings, direction):
    ans = []
    maxHeight = 0
    if direction == "EAST":
        for i in reversed(range(len(buildings))):
            if buildings[i] > maxHeight:
                ans.append(i)
                maxHeight = buildings[i]
        return ans[::-1]

    if direction == "WEST":
        for i in range(len(buildings)):
            if buildings[i] > maxHeight:
                ans.append(i)
                maxHeight = buildings[i]
        return ans


print(sunsetViews(buildings, direction))
