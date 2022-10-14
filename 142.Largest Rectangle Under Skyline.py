# Largest Rectangle Under Skyline

buildings = [1, 3, 3, 2, 4, 1, 5, 3, 2]

# Time Complexity = O(n^2) || Space Complexity = O(1)
def largestRectangleUnderSkyline(buildings):
    maxArea = 0
    for i in range(len(buildings)):
        left = i
        while left > 0 and buildings[left - 1] >= buildings[i]:
            left -= 1
        right = i
        while right < len(buildings) - 1 and buildings[right + 1] >= buildings[i]:
            right += 1

        area = (right - left + 1) * buildings[i]

        maxArea = max(area, maxArea)
    return maxArea


print(largestRectangleUnderSkyline(buildings))
