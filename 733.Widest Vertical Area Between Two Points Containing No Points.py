# Widest Vertical Area Between Two Points Containing No Points

points = [[8,7],[9,9],[7,4],[9,7]]


def maxWidthOfVerticalArea(points):
    x_sorted = sorted([x for x, _ in points])

    max_width = 0
    for i in range(len(x_sorted) - 1):
        max_width = max(max_width, x_sorted[i + 1] - x_sorted[i])

    return max_width        


print(maxWidthOfVerticalArea(points))
