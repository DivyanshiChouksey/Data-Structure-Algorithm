# Length Of Last Word
"""
    starting form end is the effective way to ans the question
    so from the end take 2 pointers and 
    then first move i through all extra spaces in right then
    start j from i and find next space and
    return the difference
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