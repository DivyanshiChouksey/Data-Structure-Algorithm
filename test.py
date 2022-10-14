from heapq import heapify, heappop, heappush


a = [1, 9, 3, 4, 7, 4, 5, 8, 2]
k = 3
heapify(a)

while k < len(a):
    heappop(a)

# k size heap
n = 25  # add
heappush(a, n)
heappop(a)

print(a[0])


# # # # print(4 ^ 4)
# # # # 100 ^ 100 # same bits zero diffent them 1
# # # """
# # # 0 0 -> 0
# # # 1 1 -> 0
# # # 1 0 -> 1
# # # 0 1 -> 1
# # #             if num in dct:
# # # [4,1,2,1,2], x = 0
# # # x = 000^ 100 -> 100 ^ 001 -> 101 ^ 010-> 111^001 -> 110 ^ 010 -> 100
# # # """
# # # s = "cbbd"


# # # def isPalin(s, i, j):
# # #     while i >= 0 and j < len(s) and s[i] == s[j]:
# # #         i -= 1
# # #         j += 1
# # #     return j - i - 1


# # # end = start = 0
# # # ans = ""
# # # for i in range(len(s)):
# # #     odd = isPalin(s, i, i)
# # #     even = isPalin(s, i, i + 1)
# # #     tmp = max(odd, even)
# # #     if tmp > end - start:
# # #         start = i - (tmp - 1) // 2
# # #         end = i + tmp // 2
# # # print(s[start : end + 1])

# # initialEnergy = 5
# # initialExperience = 3
# # energy = [1, 4, 3, 2]
# # experience = [2, 6, 3, 1]
# # energyNeeded = max(0, sum(energy) - initialEnergy + 1)
# # expNeeded = 0
# # total = initialExperience
# # for exp in experience:
# #     if exp > total:
# #         # TODO training
# #         expNeeded += exp - total + 1  # 2
# #         total += exp + expNeeded
# #     else:
# #         total += exp
# # print(energyNeeded + max(0, expNeeded))


# # # 767. Reorganize String
# # 2
# # [[2,1],[5,0],[4,2]] -> 5+2+3=>10

# # Graphs ->


# # def fun(x):
# #     return 1 if x % 2 != 0 else 2


# # print(fun(fun(1)))


# grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]


# def orangesRotting(grid):
#     r = len(grid)
#     c = len(grid[0])
#     time = 0
#     queue = []
#     freshOrange = 0
#     for i in range(r):
#         for j in range(c):
#             if grid[i][j] == 1:
#                 freshOrange += 1
#             elif grid[i][j] == 2:
#                 queue.append((i, j))

#     while queue and freshOrange:
#         tmp = []
#         for i, j in queue:
#             for m, n in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
#                 if 0 <= m < r and 0 <= n < c and grid[m][n] == 1:
#                     grid[m][n] = 2
#                     freshOrange -= 1
#                     tmp.append((m, n))

#         queue = tmp[:]
#         time += 1

#     return time if freshOrange == 0 else -1


# print(orangesRotting(grid))
