# Repeated Substring Pattern

s = "abcabcabcabc"

def repeatedSubstringPattern(s):
    t = s + s
    if s in t[1:-1]:
        return True
    return False

print(repeatedSubstringPattern(s))
