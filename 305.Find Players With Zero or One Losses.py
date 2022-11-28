# Find Players With Zero or One Losses

"""
    Create two counters to store winner players and loser players separately
    then create two set to store all players that have not lost any matches and
    all players that have lost exactly one match after that go through the winner counter and
    add winner player to set if is not in loser counter in the same way check and add loser players into 
    the another set if their count is 1 (ie. they have lost exactly one match ) 
    at the end return the sorted set as required  
"""

# Time Complexity = O(nlogn) || Space Complexity = O(n)

from collections import Counter, defaultdict

matches = [
    [1, 3],
    [2, 3],
    [3, 6],
    [5, 6],
    [5, 7],
    [4, 5],
    [4, 8],
    [4, 9],
    [10, 4],
    [10, 9],
]


def findWinners(matches):
    winner = defaultdict(int)
    loser = defaultdict(int)
    for i in range(len(matches)):
        winner[matches[i][0]] += 1
        loser[matches[i][1]] += 1

    zeroLoser = set()
    oneLoser = set()

    for k, v in winner.items():
        if k not in loser:
            zeroLoser.add(k)
        elif loser[k] == 1:
            oneLoser.add(k)

    for k, v in loser.items():
        if v == 1:
            oneLoser.add(k)

    return [sorted(zeroLoser), sorted(oneLoser)]


print(findWinners(matches))
