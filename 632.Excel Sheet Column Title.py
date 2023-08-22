# Excel Sheet Column Title

columnNumber = 701

def convertToTitle( columnNumber):
    ans = ""
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while columnNumber:
        columnNumber-=1
        ans+=s[columnNumber % 26]
        columnNumber//=26

    return ans[::-1]

print(convertToTitle( columnNumber))
