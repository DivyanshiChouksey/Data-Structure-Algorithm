# Container With Most Water

# Time Complexity = O(n), n - len(height) / 2
# Space Complexity = O(1)

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]


def maxArea(height):
    i = 0
    j = len(height) - 1

    water = 0

    while i < j:
        if height[i] < height[j]:
            tmp = height[i] * (j - i)
            i += 1
        else:
            tmp = height[j] * (j - i)
            j -= 1

        water = max(water, tmp)

    return water


print(maxArea(height))
