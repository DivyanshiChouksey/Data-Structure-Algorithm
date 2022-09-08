# Class Photos
"""
    Greedy Approach 
    sort both heights and for the front row if each element of redshirtheights or blueshirtheights
    is smaller than blueshirtheights or redshirtheights respectively then return True otherwise Flase.
"""
# Time Complexity = O(nlogn) || Space Complexity = O(1)

redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights = [6, 9, 2, 4, 5]


def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    frontRow = "RED" if redShirtHeights[0] < blueShirtHeights[0] else "BLUE"
    for i in range(len(redShirtHeights)):
        if frontRow == "RED":
            if redShirtHeights[i] >= blueShirtHeights[i]:
                return False
        else:
            if blueShirtHeights[i] >= redShirtHeights[i]:
                return False

    return True


print(classPhotos(redShirtHeights, blueShirtHeights))
