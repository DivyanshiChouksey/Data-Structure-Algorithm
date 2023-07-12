# Find Eventual Safe States


graph = [[1,2],[2,3],[5],[0],[5],[],[]]

def eventualSafeNodes(grap):
    n=len(graph)
    safe={}
    ans=[]
    def dfs(i):
        if i in safe:
            return safe[i]

        safe[i]=False
        for nei in graph[i]:
            if not dfs(nei):
                return safe[i]

        safe[i]=True
        return safe[i]

    for i in range(n):
        if dfs(i):
            ans.append(i)

    return ans  

print(eventualSafeNodes(grap))
