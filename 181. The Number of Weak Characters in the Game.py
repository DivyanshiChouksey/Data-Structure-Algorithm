# The Number Of Weak Characters in the Game
"""
    Sort the properties so that we can have the attacks in decersing order
    and keep record of current maximum defense after that go through the properties
    and increase count by 1 if the current defense is less than the current maximum defense
    at last return count. 
"""
# Time Complexity = O(nlogn) || Space Complexity = O(1)

properties = [[5, 5], [6, 3], [3, 6]]


def numberOfWeakCharacters(properties):
    properties.sort(key=lambda x: (-x[0], x[1]))
    ans = 0  # count
    curMax = 0  # store current max value
    for a, d in properties:
        if d < curMax:
            ans += 1
        else:
            curMax = d
    return ans


print(numberOfWeakCharacters(properties))
