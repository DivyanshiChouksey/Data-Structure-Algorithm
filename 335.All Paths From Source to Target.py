# All Paths From Source to Target

"""
    Recursive Solution 

"""

# Time Complexity = O(2^n) || Space Complexity = O(n)

graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]


def allPathsSourceTarget(graph):
    ans = []

    def helper(i, curarr):
        if i == len(graph) - 1:
            ans.append(curarr + [i])
            return
        else:
            for node in graph[i]:
                helper(node, curarr + [i])

    helper(0, [])
    return ans


print(allPathsSourceTarget(graph))
