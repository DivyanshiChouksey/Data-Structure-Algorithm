# Maximum Points You Can Obtain from Cards
"""
    [1,79,80,1,1,1,200,1]  k = 3
    Taking pointers one at beginning and one at the end and a variable to store the max points

    [1,79,80,1,1,1,200,1]   storing sum of k cardpoint from the beginning = 160
     * *  *
    [1,79,80,1,1,1,200,1]   now compare and store the sum of k-1 cardpoint from beginning &
     * *               *    1 cardpint from last to the pervious points = 160, (81<160) 

    [1,79,80,1,1,1,200,1]   again compare and store the sum of k-1 cardpoint from beginning &
     *              *  *    1 cardpint from last to the pervious points = 202, (160<202) 
    
    repeat the working until k > 0 and return the max points
    
"""
# Time Complexity = O(n) || Space Complexity = O(1)

cardPoints = [1,79,80,1,1,1,200,1]
k = 3

def maxPoint(cardPoints, k):
    i = 0
    j = len(cardPoints)-1
    total = sum(cardPoints[:k])
    best = total
    while k > 0:
        total += cardPoints[j] - cardPoints[k-1]
        k -= 1
        j -= 1
        if total > best:
            best = total
    return best

print(maxPoint(cardPoints,k))