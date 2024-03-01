# Maximum Odd Binary Number

s = "010"

def maximumOddBinaryNumber(s):
    cnt = 0
    for i in s:
        if i=="1":
            cnt+=1
        
    return "1"*(cnt-1) + "0"*(len(s)-cnt)+"1"
    
print(maximumOddBinaryNumber(s))
