array = [8, 4, 2, 10, 3, 6, 7, 9, 1]


def largestRange(array):
    bestRange = []
    longest


# def largestRange(array):
#     if len(array) - 1 == 0:
#         return [array[0], array[0]]
#     best = []
#     i = 0
#     r = 0
#     tmp = sorted(array)
#     l = tmp[i]
#     while l < len(array):
#         while i < len(array) - 1 and tmp[i + 1] == tmp[i] + 1:
#             r = tmp[i] + 1
#             i += 1
#         best.append([l, r])
#         l += 1
#     return max(best)


print(largestRange(array))
