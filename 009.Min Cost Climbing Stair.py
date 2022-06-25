# Min Cost Climbing Stair
"""
    as per question top floor means len(cost)th index
    so we add a zero at the last because reaching top floor from top floor cost us zero,
    Start from the last step and try to reach 1st and 2nd step 
    build a hashmap which make the record of cost and we'll go with minimum cost

"""
# Time Complexity = O(n) || Space Complexity = O(1)

cost = [10,15,20]

def minCostClimbingStair(cost):
    cost.append(0)
    for i in range(len(cost)-3,-1,-1):
        cost[i] += min(cost[i+1],cost[i+2])
    return min(cost[0],cost[1])

print(minCostClimbingStair(cost))