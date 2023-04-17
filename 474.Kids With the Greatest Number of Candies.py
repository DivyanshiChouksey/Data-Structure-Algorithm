# Kids With the Greatest Number of Candies

candies = [2,3,5,1,3]
extraCandies = 3

def kidsWithCandies(candies, extraCandies):
    maxCandy = max(candies)
    result = []
    for candy in candies:
        if candy+extraCandies >= maxCandy:
            result.append(True)
        else:
            result.append(False)

    return result

print(kidsWithCandies(candies extraCandies))
