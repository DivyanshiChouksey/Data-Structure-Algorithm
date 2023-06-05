# Number of Provinces

from collections import defaultdict,deque

isConnected = [[1,1,0],[1,1,0],[0,0,1]]

def findCircleNum(isConnected):
    dct = defaultdict(list)
    for i in range(len(isConnected)):
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1:
                dct[i].append(j)

    seen = set()
    def bfs(i):
        queue = deque([i])
        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()
                for x in dct[i]:
                    if x not in seen:
                        seen.add(x)
                        queue.append(x)
    ans = 0
    for i in range(len(isConnected)):
        if i not in seen:
            ans+=1
            bfs(i)
    return ans


print(findCircleNum(isConnected))