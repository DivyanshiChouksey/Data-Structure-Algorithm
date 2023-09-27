# Decoded String at Index

s = "ha22"
k = 5

def decodeAtIndex(s, k):
    length = 0
    i = 0
    while length < k:
        if s[i].isdigit():
            length*=int(s[i])
        else:
            length+=1
        i+=1
    
    for i in range(i-1,-1,-1):
        char = s[i]
        if char.isdigit():
            length //= int(char)
            k%=length
        elif length == k or k==0:
            return char
        else:
            length-=1



print(decodeAtIndex(s, k))

# Naive give MLE

s = "leet2code3"
k = 10

def decodeAtIndex(s, k):
  char = set("abcdefghijklmnopqrstuvwxyz")
  tmp = ""
  for i in s:
      if i in char:
          tmp+=i
      else:
          tmp+=tmp*(int(i)-1)
  return tmp[k-1]

print(decodeAtIndex(s, k))
