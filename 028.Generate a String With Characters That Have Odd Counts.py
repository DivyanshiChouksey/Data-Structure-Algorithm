# Generate a String With Characters That Have Odd Counts
"""
"""
# Time Complexity = O() || Space Complexity = O()

n = 4
str = ""
if n % 2 != 0:
    for i in range(n):
        str += "a"
else:
    for i in range(n-1):
        str += "a"
    str += "b"
print(str)