# Image Overlap

img1 = [[1, 1, 0], [0, 1, 0], [0, 1, 0]]
img2 = [[0, 0, 0], [0, 1, 1], [0, 0, 1]]

"""
    First impression this is a tough question 
    would try a naive solution then see for any valid optimization 
    Therefore, a simple idea is that one could come up all possible 
    overlapping zones, by shifting the image matrix, and then simply 
    count within each overlapping zone.
"""

# Time Complexity = O(n^4) || Space Complexity = O(1)


def largestOverlap(img1, img2):

    N = len(img1)

    def shiftCount(xMove, yMove, move, ref):
        """
        here move is matrix that we are moving
        ref is matrix we take as reference
        moving one matrix up is equivalent to
        moving the other matrix down
        """
        leftOverlap, rightOverlap = 0, 0
        for refRow, moveRow in enumerate(range(xMove, N)):
            for refCol, moveCol in enumerate(range(yMove, N)):
                if move[moveRow][moveCol] == 1 and ref[refRow][refCol] == 1:
                    leftOverlap += 1
                if move[moveRow][refCol] == 1 and ref[refRow][moveCol] == 1:
                    rightOverlap += 1
        return max(leftOverlap, rightOverlap)

    maxOverlap = 0
    for i in range(N):
        for j in range(N):
            maxOverlap = max(maxOverlap, shiftCount(j, i, img1, img2))
            maxOverlap = max(maxOverlap, shiftCount(j, i, img2, img1))
    return maxOverlap


print(largestOverlap(img1, img2))
