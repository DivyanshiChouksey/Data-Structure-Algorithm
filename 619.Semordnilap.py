# semordnilap 

from collections import defaultdict

words = ["diaper","abc","test","cba","repaid"]

def semordnilap(words):
    dct = {}
    for word in words:
        tmp = "".join(sorted(word))
        if tmp in dct:
            dct[tmp].append(word)
        else:
            dct[tmp] = [word]

    ans = []
    for k,v in dct.items():
        if len(v) > 1:
           ans.append(v) 

    return ans

print(semordnilap(words))