# Isomorphic Strings

s = "egg"
t = "add"

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dct = {}
        for c,d in zip(s,t):
            if c not in dct:
                dct[c] = d
            if dct[c] !=d:
                return False
        dct = {}
        for d,c in zip(s,t):
            if c not in dct:
                dct[c] = d
            if dct[c]!=d:
                return False
        return True
