# Construct Target Array With Multiple Sum
"""
    main aim is to find maximum value every time
    and that can be done by heap in O(logn) time
    
    [5,33,17,x,57]   x = 113 - (5+33+17+57) = 1
    [5,33,17,1,x]    x = 57 - (5+33+17+1)   = 1
    [5,x,17,1,1]     x = 33 - (5+17+1+1)    = 9
    [5,9,x,1,1]      x = 17 - (5+9+1+1)     = 1
    [5,x,1,1,1]      x = 9 - (5+1+1+1)      = 1
    [x,1,1,1,1]      x = 5 - (1+1+1+1)      = 1
    [1,1,1,1,1]
"""
# Time Complexity = O(nlogn) || Space Complexity = O(1)

target = [9,3,5]

def isPossible(target) :

    import heapq

    total = sum(target)

    for i in range (len(target)):   #target = [-a for a in target]
        target[i] *= (-1)
    heapq.heapify(target)

    while True:
        x = -heapq.heappop(target)
        total -= x   # now total = 8 and x = 9
        if x == 1 or total == 1 :
            return True
        if total > x or total == 0 or total == x:
            return False
        x %= total
        total += x
        heapq.heappush(target,-x)

    
print(isPossible(target))


