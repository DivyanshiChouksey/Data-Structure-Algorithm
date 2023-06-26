# Total Cost to Hire K Workers

import heapq

costs = [17,12,10,2,7,2,11,20,8]
k = 3
candidates = 4

def totalCost(costs, k, candidates):
    q = costs[:candidates]
    qq = costs[max(candidates, len(costs)-candidates):]
    heapify(q)
    heapify(qq)
    ans = 0 
    i, ii = candidates, len(costs)-candidates-1
    for _ in range(k): 
        if not qq or q and q[0] <= qq[0]: 
            ans += heappop(q)
            if i <= ii: 
                heappush(q, costs[i])
                i += 1
        else: 
            ans += heappop(qq)
            if i <= ii: 
                heappush(qq, costs[ii])
                ii -= 1
    return ans 

print(totalCost(costs, k, candidates))
