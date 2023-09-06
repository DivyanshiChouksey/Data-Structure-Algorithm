# # Multiple Graphs 
# from collections import Counter, defaultdict

# n = 3
# grid = [[1,3,4,5],[7,2,3,4],[1,3,2,1]]

# # def helper(grid):
# # win = Counter()
# dct = defaultdict(int)
# for i in range(len(grid[0])):
#     tmp = []
#     for j in range(len(grid)):
#         tmp.append((grid[j][i],j+1))
#     tmp.sort()
#     dct[tmp[-1][1]]+=1

# print(dct)


width = 4
height = 3

ways = [[1 for _ in range(width)]for _ in range(height)]
print(ways)
for i in range(1,height):
    for j in range(1,width):
        ways[i][j] = ways[i-1][j]+ways[i][j-1]
        print(ways)

print(ways[-1][-1])