# Find Players With Zero or One Losses

from collections import defaultdict

matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]

def findWinners(matches):
    winner = DefaultDict(int)
    loser = DefaultDict(int)
    for win,los in matches:
        winner[win]+=1
        loser[los]+=1
    print(winner,loser)
    ans = []
    tmp = set()
    tmp2 = set()
    for val,count in winner.items():
        if val not in loser:
            tmp.add(val)
        
        elif loser[val]==1:
            tmp2.add(val)
    for val,count in loser.items():
        if count==1 and val not in tmp2:
            tmp2.add(val)
    tmp = list(tmp)
    tmp.sort()
    tmp2 = list(tmp2)
    tmp2.sort()
    return [tmp,tmp2]


print( findWinners(matches))
