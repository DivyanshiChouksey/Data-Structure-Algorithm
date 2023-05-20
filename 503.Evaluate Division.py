# Evaluate Division

from collections import defaultdict

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

def calcEquation(equations, values, queries):
    """
    We can see that we are given values of a/b so we make a weighted graph 
    representing a->b with w and b->a with 1/w
    {
        'a': {'b': 2.0}, 
        'b': {'a': 0.5, 'c': 3.0}, 
        'c': {'b': 0.3333333333333333,'d': 2}
        'd': {'c': 0.5}
    )
    """
    
    graph = defaultdict(dict)
    for (x,y),val in zip(equations,values):
        graph[x][y] = val
        graph[y][x] = 1/val


    # x = b, y = d
    def dfs(x,y,visited):
        if x not in graph or y not in graph:
            return -1
        
        if y in graph[x]: # we can directly visit it
            return graph[x][y]

        # if we cannot find it directly then search for other way around do dfs
        for i in graph[x]:
            if i not in visited:
                visited.add(i)
                tmp = dfs(i,y,visited)
                if tmp == -1:
                    continue
                else:
                    return graph[x][i] * tmp

        return -1

    res = []
    for q in queries:
        res.append(dfs(q[0],q[1],set())) # here set() = viisited / seen set 
    return res

print(calcEquation(equations, values, queries))