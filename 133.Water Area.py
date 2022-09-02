# Water Area

# Naive Solution
"""
    Main concept in this question is to find place and amount of water that can be trap betwen two pillars 
    so logically we can only trap the max water as much as smallest height of pillar we have between two pillars 
    for more clearity go through the example given below

    height    = [0,  8,  0,  0,  5,  0,  0,  10,  0,  0,  1,  1,  0,  3]  - heights of pillars at i th index

    leftMax   = [0,  8,  8,  8,  8,  8,  8,  10, 10, 10, 10, 10, 10, 10]    at each index we store the tallest pillar to 
                                                                            the left of the current index that we're at                                           
                                                                            
    rightMax  = [10, 10, 10, 10, 10, 10, 10, 10,  3,  3,  3,  3,  3,  3]    at each index we store the tallest pillar to 
                                                                            the right of the current index that we're at
                                                                                                                                            
    waterArea = [ 0,  0,  8,  8,  3,  8,  8,  0,  3,  3,  2,  2,  3,  0]    then at each index of water area will store min height 
                                                                            betwen leftMax and rightMax minus the current height
                                                                            if min height is smaller than the current height else store 
                                                                            zero amount of water because then only water will spill out.
                                                                                                                                                                                                                                  
    and return sum of waterArea
"""

# Time Complexity = O(n) || Space Complexity = O(n)


height = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]


def waterArea(height):
    maxes = [0 for i in range(len(height))]
    leftMax = 0
    for i in range(len(height)):
        maxes[i] = leftMax
        leftMax = max(leftMax, height[i])

    rightMax = 0
    for i in reversed(range(len(height))):
        minHeight = min(rightMax, maxes[i])
        if height[i] < minHeight:
            maxes[i] = minHeight - height[i]
        else:
            maxes[i] = 0

        rightMax = max(rightMax, height[i])
    return sum(maxes)


print(waterArea(height))
