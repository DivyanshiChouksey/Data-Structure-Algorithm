# Path with Maximum Probability

from collection import defaultdict
import heapq

n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]start = 0
end = 2


def maxProbability(n, edges, succProb, start, end):
    dct = defaultdict(list)
    for i,(u,v) in enumerate(edges):
        dct[u].append((v,succProb[i]))
        dct[v].append((u,succProb[i]))

    maxProb = [0.0]*n
    maxProb[start] = 1.0

    pq = [(-1.0,start)]

    while pq:
        curProb, curNode = heapq.heappop(pq)
        if curNode == end:
            return -curProb
        for nxt,path in dct[curNode]:
            if -curProb * path > maxProb[nxt]:
                maxProb[nxt] = -curProb*path
                heapq.heappush(pq,(-maxProb[nxt],nxt))
    return 0.0    


print(maxProbability(n, edges, succProb, start, end))
            
