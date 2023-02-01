# Greatest Common Divisor of Strings

"""
    Hit and Try 
    if str1 = str2 return str2
    decrease the str2 one by one and check.

"""

# Time Complexity = O(min(m,n)*(m+n))  , n = len(str1) 
# Space Complexity = O(m+n)     , m = len(str2) 

str1 = "ABABAB"
str2 = "ABAB"

def gcdOfStrings(str1,str2):
    for i in range(min(len(str1),len(str2)),0,-1):
        tmp = str2[:i] 
        if tmp*(len(str2) // i )== str2:
            if tmp*(len(str1) // i) == str1:
                return tmp
    return ""
    

print(gcdOfStrings(str1,str2))