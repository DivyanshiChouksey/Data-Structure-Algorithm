# Maximum Weight Node

from collections import Counter,defaultdict

edges = [4, 4, 1, 4, 13, 8 ,8, 8, 0, 8, 14 ,9 ,15, 11, -1, 10, 15, 22, 22, 22, 22, 22, 21]


# Solution 1

tmp = Counter(edges).most_common()
print(tmp)
print(tmp[0][0])


# Solution 2 (using graph)

dct = defaultdict(list)
for i in range(len(edges)):
    dct[edges[i]].append(i)

ans = float("-inf")
for k,v in dct.items():
    if len(v) > ans:
        ans = k

print(ans)