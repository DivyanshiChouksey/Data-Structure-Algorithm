# Implement StrStr()
"""

"""
# Time Complexity = O() || Space Complexity = O()

haystack = "hello"
needle = "ll"

def implement(haystack , needle):
    n = len(needle)
    for i in range(len(haystack)-n+1):
        if needle == haystack[i:i+n]:
            return i
    return -1

print(implement(haystack , needle))