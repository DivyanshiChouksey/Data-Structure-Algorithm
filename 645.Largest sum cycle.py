# Largest sum cycle

edges = [4, 4, 1, 4, 13, 8 ,8, 8, 0, 8, 14 ,9 ,15, 11, -1, 10, 15, 22, 22, 22, 22, 22, 21]

n = len(edges)
max_length = float('-inf')
seen = [False] * n
visiting = {}
stack = []
        
def dfs(node):
    global max_length 
    if not seen[node]:
        if node in visiting:
            max_length = max(max_length, len(stack) - visiting[node])
        elif edges[node] != -1: 
            visiting[node] = len(stack) 
            stack.append(node)
            dfs(edges[node])
            stack.pop()
            visiting.pop(node)
        seen[node] = True

for i in range(n):            
    dfs(i)
# return self.max_length if max_length > 0 else -1
print(max_length) 
    