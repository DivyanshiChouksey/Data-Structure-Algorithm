# Word Pattern

# Time Complexity = O() || Space Complexity = O()
pattern = "abba"
s = "dog cat cat dog"


def wordPattern(pattern, s):
    s = s.split()

    if len(pattern) != len(s):
        return False

    dct = {}
    for i, j in zip(pattern, s):
        if i in dct and dct[i] != j:
            return False
        elif i not in dct:
            if j in dct.values():
                return False
            dct[i] = j

    return True


print(wordPattern(pattern, s))
