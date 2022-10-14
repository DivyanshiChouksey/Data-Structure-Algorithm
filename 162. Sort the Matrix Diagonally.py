from collections import defaultdict


mat = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
dct = defaultdict(list)
for i in range(len(mat)):
    for j in range(len(mat[0])):
        dct[j - i].append(mat[i][j])

for k in dct:
    dct[k].sort(reverse=True)
for i in range(len(mat)):
    for j in range(len(mat[0])):
        mat[i][j] = dct[j - i].pop()

print(mat)
