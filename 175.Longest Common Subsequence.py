# Longest Common Subsequence

str1 = "ZXVVYZW"
str2 = "XKYKZPW"

# Time Complexity = O(n*m) , n - len(str1)
# Space Complexity = O(n*m), m - len(str2)


def longestCommonSubsequence(str1, str2):
    lcs = [[[] for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + [str2[i - 1]]
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1], key=len)
    return lcs[-1][-1]


print(longestCommonSubsequence(str1, str2))


# output  - ['X', 'Y', 'Z', 'W']
