# Interleaving String

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"


def isInterleave( one, two, three):
    """
      0 1 2
  s1= a a a

    a a a f
    0 1 2 3 

    a a a f a a a
    0 1 2 3 4 5 6

    [ , , , ]
    [ , , , ]
    [ , , , ]
    [ , , , ]
    
    a
    
    """
        
    if len(three) != len(one)+ len(two):
        return False

    cache = [[None for j in range(len(two)+1)]for i in range(len(one)+1)]
    def helper(one,two,three,i,j, cache):
        if cache[i][j] is not None:
            return cache[i][j]
        
        k = i+j
        if k==len(three):
            return True

        if i<len(one) and one[i] == three[k]:
            cache[i][j] = helper(one, two, three, i+1, j, cache)
            if cache[i][j]:
                return True

        if j<len(two) and two[j] == three[k]:
            cache[i][j] = helper(one, two,three, i, j+1, cache)
            return cache[i][j]

        cache[i][j] = False
        return False
        
    return helper(one, two, three, 0, 0, cache)


print(isInterleave( one, two, three))
