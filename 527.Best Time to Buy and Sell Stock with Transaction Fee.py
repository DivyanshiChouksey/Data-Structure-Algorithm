# Best Time to Buy and Sell Stock with Transaction Fee

prices = [1,3,2,8,4,9]
fee = 2

def maxProfit(self, prices: List[int], fee: int) -> int:
    n=len(prices)
    # dp=[[0]*2 for i in range(n+1)]
    ahd=[0]*2
    for i in range(n-1,-1,-1):
        curr=[0]*2
        for j in range(1,-1,-1):
            if j==1:
                curr[j]=max(ahd[j],ahd[0]-prices[i])
            else:
                curr[j]=max(ahd[j],ahd[1]+prices[i]-fee)
        ahd=curr
    return ahd[1]
