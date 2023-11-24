# Maximum Number of Coins You Can Get

piles = [9,8,7,6,5,1,2,3,4]


def maxCoins(piles):

    # 9 8 7 6 5 4 3 2 1
    # 9 8 1
    # 7 6 2  
    # 5 4 3 

    piles.sort(reverse=True)
    i = 1
    j = len(piles)-1
    ans = 0
    while i<=j:
        ans+=piles[i]
        i+=2
        j-=1

    return ans


print(maxCoins(piles))
