# Zigzag Conversion

"""
    Iterate through ss from left to right, appending each character to the appropriate row. The appropriate row can be tracked using two variables: the current row and the current direction.
    The current direction changes only when we moved up to the topmost row or moved down to the bottommost row.
"""

# Time Complexity = O(n) || Space Complexity = O(n)

s = "PAYPALISHIRING"
numRows = 4

def convert( s, numRows):
    # ['PIN', 'ALSIG', 'YAHR', 'PI']
    ans = [""]*numRows
    goingDown = True
    i = 0
    j= 0
    for ch in s:
        if goingDown:
            ans[i] += ch
            i+=1
            if i==numRows:
                goingDown = False
                # j = numRow-2
                i-=1
        else:
            ans[i] += ch
            i-=1
            if i==1:
                goingDown=True
                i=0
    return ans


print(convert( s, numRows))