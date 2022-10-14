from typing import Counter


nums = [3, 1, 4, 4, 5, 2, 6, 1]
K = 2
cnt = Counter(nums)
for k, v in cnt.items():
    # if K == 0:
    #     break
    print(k, v)
    # K -= 1
print(cnt)


# array = [
#     [0, 0, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 0, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0],
# ]
# source = 3


# def waterfallStreams(array, source):
#     above = array[0][:]
#     above[source] = -1
#     for i in range(1, len(array)):
#         current = array[i][:]
#         for j in range(len(above)):
#             value = above[j]
#             hasWater = value < 0
#             hasBlock = current[j] == 1
#             if not hasWater:
#                 continue
#             if not hasBlock:
#                 current[j] += value
#                 continue
#             splitWater = value / 2
#             right = j
#             while right + 1 < len(array):
#                 right += 1
#                 if above[right] == 1:
#                     break
#                 if current[right] != 1:
#                     current[right] += splitWater
#                     break

#             left = j
#             while left - 1 >= 0:
#                 left -= 1
#                 if above[left] == 1:
#                     break
#                 if current[left] != 1:
#                     current[left] += splitWater
#                     break

#         above = current
#     return list(map(lambda x: x * -100, above))


# print(waterfallStreams(array, source))
