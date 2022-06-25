# Length Of Last Word
"""
    starting form last is the effective way to ans the ques
    take two pointers if it is space just ahead else increase the length
"""
# Time Complexity = O(n) || Space Complexity = O(1)

s = "  fly me   to  the moon  "

def LengthOfLastWord(s):
    i , length = len(s)-1 , 0
    while s[i] == " ":
        i -= 1
    while i >= 0 and s[i] != " ":
        length += 1
        i -= 1
    return length

print(LengthOfLastWord(s))