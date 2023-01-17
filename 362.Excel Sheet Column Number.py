# Excel Sheet Column Number

# Time Complexity = O(n) || Space Complexity = O(1)


columnTitle = "ABCD"


def titleToNumber(columnTitle):
    ans = 0
    for ch in columnTitle:
        ans *= 26
        i = ord(ch) - 64
        ans = ans + i
    return ans


print(titleToNumber(columnTitle))
