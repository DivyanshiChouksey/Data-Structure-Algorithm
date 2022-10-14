# Edit Distance
"""

"""
# Time Complexity = O() || Space Complexity = O()

str1 = "horse"
str2 = "ros"


def editDistance(str1, str2):
    ed = [[0 for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]
    # print(ed)
    for i in range(len(str1) + 1):
        ed[0][i] = i
    for j in range(len(str2) + 1):
        ed[j][0] = j
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                ed[j][i] = ed[j - 1][i - 1]
            else:
                ed[j][i] = min(ed[j - 1][i - 1], ed[j - 1][i], ed[j][i - 1]) + 1

    return ed[-1][-1]


print(editDistance(str1, str2))
