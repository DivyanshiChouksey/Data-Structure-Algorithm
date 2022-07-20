# Assign Cookies
"""
    We check that size should be greater or equal to the greedy factor of the Cookies
    for the maximum number of content children.
"""
# Time Complexity = O()
g = [1, 2, 3]
s = [4, 6, 7]


def findContentChildren(g, s):
    g.sort()
    s.sort()
    i = 0
    j = 0
    while i < len(s) and j < len(g):
        if s[i] >= g[j]:
            i += 1
        j += 1
    return i


print(findContentChildren(g, s))
