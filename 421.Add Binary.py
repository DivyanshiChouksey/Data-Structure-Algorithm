# Add Binary
    
"""
    1 0 0 => 1
    1 1 1 => 11 
    1 1 0 => 10
    0 0 0 => 0

"""
a = "1010"
b = "1011"

def addBinary(a, b):
    a = a[::-1]
    b = b[::-1]
    ans = ""
    i = 0
    carry = 0
    while i<max(len(a),len(b)) or carry: 
        a1,b1 =0,0
        if i<len(a):
            a1 = int(a[i])
        if i<len(b):
            b1 = int(b[i])
        if a1+b1+carry == 1:
            carry = 0
            ans+="1"
        elif a1+b1+carry == 2:
            carry = 1
            ans+="0"
        elif a1+b1+carry == 3:
            carry = 1
            ans+="1"
        else:
            carry = 0
            ans+="0"
        i+=1
    return ans[::-1]

print(addBinary(a, b))