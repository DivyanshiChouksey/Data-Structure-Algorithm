# Possible Bipartition

"""
    ** Very Classical graph coloring problem 
    step 1 - Create a adjacency list inside the 2D array
            like - ith index contain the list of people which are disliked by the ith person

    step 2 - now using concept of the Bipartite Graph coloring problem
            create an array which keep track of color of ith person
            
    step 3 - for creating the array allocate the color to the persons by checking two condition:-
                1. if dislike persons by the ith person have no color then allocate them opposite color
                2. ith person and the dislike persons by the ith person do not have the same color
                   if they have same color then return False otherwise return True.  

"""

# Time Complexity = O(n) || Space Complexity = O(n)

n = 5
dislikes = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]


def possibleBipartition(n, dislikes):
    g = [[] for _ in range(n + 1)]
    for n1, n2 in dislikes:
        g[n1].append(n2)
        g[n2].append(n1)
    # print(g)
    color = [0] * (len(g))  # => [0, 1, -1, -1, 1]
    for i in range(1, len(g)):
        if color[i]:
            continue
        queue = [i]
        color[i] = 1
        while queue:
            node = queue.pop()
            for adj in g[node]:
                if color[node] == color[adj]:
                    # print(False)
                    return False
                elif color[adj] == 0:
                    queue.append(adj)
                    color[adj] = -color[node]

    return True


print(possibleBipartition(n, dislikes))
