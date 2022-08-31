# Kids With The Greatest Number Of Candies
"""
    Return true if the current candies plus extraCandies is greater than max of candies
    else return False
"""
# Time Complexity = O(n) || Space Complexity = O(n)

candies = [2, 3, 5, 1, 3]
extraCandies = 3


def kidsWithCandies(candies, extraCandies):
    maxCandy = max(candies)
    ans = []
    for i in range(len(candies)):
        if candies[i] + extraCandies >= maxCandy:
            ans.append(True)
        else:
            ans.append(False)

    return ans


def kidsWithCandies2(candies, extraCandies):
    maxCandy = max(candies) - extraCandies
    ans = []
    for candy in candies:
        if candy >= maxCandy:
            ans.append(True)
        else:
            ans.append(False)
    return ans


print(kidsWithCandies(candies, extraCandies))
print(kidsWithCandies2(candies, extraCandies))
